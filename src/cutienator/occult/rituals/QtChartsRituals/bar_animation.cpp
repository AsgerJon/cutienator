//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/baranimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/baranimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A BarAnimation that Python can take functions over in. Every BarAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteBarAnimationCall0)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteBarAnimationCall1)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteBarAnimationCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteBarAnimationCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteBarAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteBarAnimationCall5)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteBarAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBarAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBarAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteBarAnimation : public BarAnimation {
public:
  using BarAnimation::BarAnimation;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN17QVariantAnimation18updateCurrentValueERK8QVariant")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK18QAbstractAnimation8durationEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation17updateCurrentTimeEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation11updateStateENS_5StateES0_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation15updateDirectionENS_9DirectionE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(animation)
  //  QVariant BarAnimation::interpolated(const QVariant &from, const
  //      QVariant &to, qreal progress) const
  QVariant interpolated(
      const QVariant &from,
      const QVariant &to,
      qreal progress) const override {
    if (taken[0]) {
      int handled = 0;
      CuteBarAnimationCall0 call = reinterpret_cast<CuteBarAnimationCall0>(taken[0]);
      const QVariant * given = call(this, &from, &to, progress, &handled);
      if (handled && given) return *given;
    }
    return BarAnimation::interpolated(from, to, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void BarAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteBarAnimationCall1 call = reinterpret_cast<CuteBarAnimationCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
    BarAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[2]) {
      int handled = 0;
      CuteBarAnimationCall2 call = reinterpret_cast<CuteBarAnimationCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QVariantAnimation::duration();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  bool QVariantAnimation::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteBarAnimationCall3 call = reinterpret_cast<CuteBarAnimationCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QVariantAnimation::event(event);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  void QVariantAnimation::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteBarAnimationCall4 call = reinterpret_cast<CuteBarAnimationCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QVariantAnimation::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QVariantAnimation::updateState(QAbstractAnimation::State
  //      newState, QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[5]) {
      int handled = 0;
      CuteBarAnimationCall5 call = reinterpret_cast<CuteBarAnimationCall5>(taken[5]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QVariantAnimation::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void
  //      QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
  //      direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[6]) {
      int handled = 0;
      CuteBarAnimationCall6 call = reinterpret_cast<CuteBarAnimationCall6>(taken[6]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimation::updateDirection(direction);
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteBarAnimationCall7 call = reinterpret_cast<CuteBarAnimationCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteBarAnimationCall8 call = reinterpret_cast<CuteBarAnimationCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteBarAnimationCall9 call = reinterpret_cast<CuteBarAnimationCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteBarAnimationCall10 call = reinterpret_cast<CuteBarAnimationCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteBarAnimationCall11 call = reinterpret_cast<CuteBarAnimationCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteBarAnimationCall12 call = reinterpret_cast<CuteBarAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *BarAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12BarAnimation10metaObjectEv(
    const BarAnimation *self) {
  return self->metaObject();
}

//  void *BarAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12BarAnimation11qt_metacastEPKc(
    BarAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int BarAnimation::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12BarAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    BarAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString BarAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12BarAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(BarAnimation::tr(s, c, n));
}

//  BarAnimation::BarAnimation(AbstractBarChartItem *item, int duration,
//      QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
BarAnimation *ritual_ZN12BarAnimationC1EP20AbstractBarChartItemiR12QEasingCurve(
    AbstractBarChartItem *item,
    int duration,
    QEasingCurve *curve) {
  return new CuteBarAnimation(item, duration, *curve);
}

//  BarAnimation::~BarAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarAnimationD1Ev(BarAnimation *self) {
  delete self;
}

//  QVariant BarAnimation::interpolated(const QVariant &from, const QVariant
//      &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12BarAnimation12interpolatedERK8QVariantS2_d(
    const BarAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(self->interpolated(*from, *to, progress));
}

//  void BarAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarAnimation18updateCurrentValueERK8QVariant(
    BarAnimation *self,
    const QVariant *value) {
  self->updateCurrentValue(*value);
}

//  void BarAnimation::setup(const QList<QRectF> &oldLayout, const
//      QList<QRectF> &newLayout)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarAnimation5setupERK5QListI6QRectFES4_(
    BarAnimation *self,
    const QList<QRectF> *oldLayout,
    const QList<QRectF> *newLayout) {
  self->setup(*oldLayout, *newLayout);
}

//  a Python function taken by a CuteBarAnimation, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_BarAnimation(
    BarAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteBarAnimation *>(self)->take(key, call);
}

//  QVariant BarAnimation::interpolated(const QVariant &from, const QVariant
//      &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK12BarAnimation12interpolatedERK8QVariantS2_d(
    const BarAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(
      self->BarAnimation::interpolated(
          *from,
          *to,
          progress));
}

//  void BarAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12BarAnimation18updateCurrentValueERK8QVariant(
    BarAnimation *self,
    const QVariant *value) {
  self->BarAnimation::updateCurrentValue(*value);
}

#endif  // QT_CONFIG(charts_bar_chart)
