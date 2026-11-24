//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/scatteranimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/scatteranimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on ScatterAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnScatterAnimation : ScatterAnimation {
  using ScatterAnimation::updateState;
};

//  A ScatterAnimation that Python can take functions over in. Every ScatterAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef void (*CuteScatterAnimationCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteScatterAnimationCall1)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteScatterAnimationCall2)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteScatterAnimationCall3)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteScatterAnimationCall4)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteScatterAnimationCall5)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteScatterAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteScatterAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteScatterAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteScatterAnimation : public ScatterAnimation {
public:
  using ScatterAnimation::ScatterAnimation;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation11updateStateENS_5StateES0_")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN17QVariantAnimation18updateCurrentValueERK8QVariant")) {
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
  //  void ScatterAnimation::updateState(QAbstractAnimation::State
  //      newState, QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[0]) {
      int handled = 0;
      CuteScatterAnimationCall0 call = reinterpret_cast<CuteScatterAnimationCall0>(taken[0]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    ScatterAnimation::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  QVariant XYAnimation::interpolated(const QVariant &start, const
  //      QVariant &end, qreal progress) const
  QVariant interpolated(
      const QVariant &start,
      const QVariant &end,
      qreal progress) const override {
    if (taken[1]) {
      int handled = 0;
      CuteScatterAnimationCall1 call = reinterpret_cast<CuteScatterAnimationCall1>(taken[1]);
      const QVariant * given = call(this, &start, &end, progress, &handled);
      if (handled && given) return *given;
    }
    return XYAnimation::interpolated(start, end, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void XYAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteScatterAnimationCall2 call = reinterpret_cast<CuteScatterAnimationCall2>(taken[2]);
      call(this, &value, &handled);
      if (handled) return;
    }
    XYAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[3]) {
      int handled = 0;
      CuteScatterAnimationCall3 call = reinterpret_cast<CuteScatterAnimationCall3>(taken[3]);
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
      CuteScatterAnimationCall4 call = reinterpret_cast<CuteScatterAnimationCall4>(taken[4]);
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
      CuteScatterAnimationCall5 call = reinterpret_cast<CuteScatterAnimationCall5>(taken[5]);
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
      CuteScatterAnimationCall6 call = reinterpret_cast<CuteScatterAnimationCall6>(taken[6]);
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
      CuteScatterAnimationCall7 call = reinterpret_cast<CuteScatterAnimationCall7>(taken[7]);
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
      CuteScatterAnimationCall8 call = reinterpret_cast<CuteScatterAnimationCall8>(taken[8]);
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
      CuteScatterAnimationCall9 call = reinterpret_cast<CuteScatterAnimationCall9>(taken[9]);
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
      CuteScatterAnimationCall10 call = reinterpret_cast<CuteScatterAnimationCall10>(taken[10]);
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
      CuteScatterAnimationCall11 call = reinterpret_cast<CuteScatterAnimationCall11>(taken[11]);
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
      CuteScatterAnimationCall12 call = reinterpret_cast<CuteScatterAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  ScatterAnimation::~ScatterAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterAnimationD1Ev(ScatterAnimation *self) {
  delete self;
}

//  void ScatterAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    ScatterAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  self->updateState(newState, oldState);
}

//  a Python function taken by a CuteScatterAnimation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ScatterAnimation(
    ScatterAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteScatterAnimation *>(self)->take(key, call);
}

//  void ScatterAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16ScatterAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    ScatterAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  static_cast<OwnScatterAnimation *>(self)->OwnScatterAnimation::updateState(
      newState,
      oldState);
}
