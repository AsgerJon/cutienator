//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/splineanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_spline_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/splineanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on SplineAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnSplineAnimation : SplineAnimation {
  using SplineAnimation::interpolated;
  using SplineAnimation::updateCurrentValue;
  using SplineAnimation::updateState;
};

//  A SplineAnimation that Python can take functions over in. Every SplineAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteSplineAnimationCall0)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteSplineAnimationCall1)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteSplineAnimationCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteSplineAnimationCall3)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteSplineAnimationCall4)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteSplineAnimationCall5)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteSplineAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSplineAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSplineAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSplineAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSplineAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSplineAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSplineAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteSplineAnimation : public SplineAnimation {
public:
  using SplineAnimation::SplineAnimation;
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
    if (!std::strcmp(key, "_ZN18QAbstractAnimation11updateStateENS_5StateES0_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK18QAbstractAnimation8durationEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation17updateCurrentTimeEi")) {
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
  //  QVariant SplineAnimation::interpolated(const QVariant &start, const
  //      QVariant &end, qreal progress) const
  QVariant interpolated(
      const QVariant &start,
      const QVariant &end,
      qreal progress) const override {
    if (taken[0]) {
      int handled = 0;
      CuteSplineAnimationCall0 call = reinterpret_cast<CuteSplineAnimationCall0>(taken[0]);
      const QVariant * given = call(this, &start, &end, progress, &handled);
      if (handled && given) return *given;
    }
    return SplineAnimation::interpolated(start, end, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void SplineAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteSplineAnimationCall1 call = reinterpret_cast<CuteSplineAnimationCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
    SplineAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void SplineAnimation::updateState(QAbstractAnimation::State newState,
  //      QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[2]) {
      int handled = 0;
      CuteSplineAnimationCall2 call = reinterpret_cast<CuteSplineAnimationCall2>(taken[2]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    SplineAnimation::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[3]) {
      int handled = 0;
      CuteSplineAnimationCall3 call = reinterpret_cast<CuteSplineAnimationCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteSplineAnimationCall4 call = reinterpret_cast<CuteSplineAnimationCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteSplineAnimationCall5 call = reinterpret_cast<CuteSplineAnimationCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QVariantAnimation::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void
  //      QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
  //      direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[6]) {
      int handled = 0;
      CuteSplineAnimationCall6 call = reinterpret_cast<CuteSplineAnimationCall6>(taken[6]);
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
      CuteSplineAnimationCall7 call = reinterpret_cast<CuteSplineAnimationCall7>(taken[7]);
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
      CuteSplineAnimationCall8 call = reinterpret_cast<CuteSplineAnimationCall8>(taken[8]);
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
      CuteSplineAnimationCall9 call = reinterpret_cast<CuteSplineAnimationCall9>(taken[9]);
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
      CuteSplineAnimationCall10 call = reinterpret_cast<CuteSplineAnimationCall10>(taken[10]);
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
      CuteSplineAnimationCall11 call = reinterpret_cast<CuteSplineAnimationCall11>(taken[11]);
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
      CuteSplineAnimationCall12 call = reinterpret_cast<CuteSplineAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  SplineAnimation::SplineAnimation(SplineChartItem *item, int duration,
//      QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
SplineAnimation *ritual_ZN15SplineAnimationC1EP15SplineChartItemiR12QEasingCurve(
    SplineChartItem *item,
    int duration,
    QEasingCurve *curve) {
  return new CuteSplineAnimation(item, duration, *curve);
}

//  SplineAnimation::~SplineAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineAnimationD1Ev(SplineAnimation *self) {
  delete self;
}

//  void SplineAnimation::setup(const QList<QPointF> &oldPoints, const
//      QList<QPointF> &newPoints, const QList<QPointF> &oldContorlPoints,
//      const QList<QPointF> &newControlPoints, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineAnimation5setupERK5QListI7QPointFES4_S4_S4_i(
    SplineAnimation *self,
    const QList<QPointF> *oldPoints,
    const QList<QPointF> *newPoints,
    const QList<QPointF> *oldContorlPoints,
    const QList<QPointF> *newControlPoints,
    int index) {
  self->setup(
      *oldPoints,
      *newPoints,
      *oldContorlPoints,
      *newControlPoints,
      index);
}

//  QVariant SplineAnimation::interpolated(const QVariant &start, const
//      QVariant &end, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15SplineAnimation12interpolatedERK8QVariantS2_d(
    const SplineAnimation *self,
    const QVariant *start,
    const QVariant *end,
    qreal progress) {
  return new QVariant(self->interpolated(*start, *end, progress));
}

//  void SplineAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineAnimation18updateCurrentValueERK8QVariant(
    SplineAnimation *self,
    const QVariant *value) {
  self->updateCurrentValue(*value);
}

//  void SplineAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    SplineAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  self->updateState(newState, oldState);
}

//  a Python function taken by a CuteSplineAnimation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_SplineAnimation(
    SplineAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteSplineAnimation *>(self)->take(key, call);
}

//  QVariant SplineAnimation::interpolated(const QVariant &start, const
//      QVariant &end, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK15SplineAnimation12interpolatedERK8QVariantS2_d(
    const SplineAnimation *self,
    const QVariant *start,
    const QVariant *end,
    qreal progress) {
  return new QVariant(
      static_cast<const OwnSplineAnimation *>(self)->OwnSplineAnimation::interpolated(
          *start,
          *end,
          progress));
}

//  void SplineAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineAnimation18updateCurrentValueERK8QVariant(
    SplineAnimation *self,
    const QVariant *value) {
  static_cast<OwnSplineAnimation *>(self)->OwnSplineAnimation::updateCurrentValue(
      *value);
}

//  void SplineAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    SplineAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  static_cast<OwnSplineAnimation *>(self)->OwnSplineAnimation::updateState(
      newState,
      oldState);
}

#endif  // QT_CONFIG(charts_spline_chart)
