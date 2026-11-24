//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/axisanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/axisanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on AxisAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAxisAnimation : AxisAnimation {
  using AxisAnimation::interpolated;
  using AxisAnimation::updateCurrentValue;
};

//  A AxisAnimation that Python can take functions over in. Every AxisAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteAxisAnimationCall0)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteAxisAnimationCall1)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteAxisAnimationCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteAxisAnimationCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteAxisAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteAxisAnimationCall5)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteAxisAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAxisAnimation : public AxisAnimation {
public:
  using AxisAnimation::AxisAnimation;
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
  //  QVariant AxisAnimation::interpolated(const QVariant &from, const
  //      QVariant &to, qreal progress) const
  QVariant interpolated(
      const QVariant &from,
      const QVariant &to,
      qreal progress) const override {
    if (taken[0]) {
      int handled = 0;
      CuteAxisAnimationCall0 call = reinterpret_cast<CuteAxisAnimationCall0>(taken[0]);
      const QVariant * given = call(this, &from, &to, progress, &handled);
      if (handled && given) return *given;
    }
    return AxisAnimation::interpolated(from, to, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void AxisAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteAxisAnimationCall1 call = reinterpret_cast<CuteAxisAnimationCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
    AxisAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[2]) {
      int handled = 0;
      CuteAxisAnimationCall2 call = reinterpret_cast<CuteAxisAnimationCall2>(taken[2]);
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
      CuteAxisAnimationCall3 call = reinterpret_cast<CuteAxisAnimationCall3>(taken[3]);
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
      CuteAxisAnimationCall4 call = reinterpret_cast<CuteAxisAnimationCall4>(taken[4]);
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
      CuteAxisAnimationCall5 call = reinterpret_cast<CuteAxisAnimationCall5>(taken[5]);
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
      CuteAxisAnimationCall6 call = reinterpret_cast<CuteAxisAnimationCall6>(taken[6]);
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
      CuteAxisAnimationCall7 call = reinterpret_cast<CuteAxisAnimationCall7>(taken[7]);
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
      CuteAxisAnimationCall8 call = reinterpret_cast<CuteAxisAnimationCall8>(taken[8]);
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
      CuteAxisAnimationCall9 call = reinterpret_cast<CuteAxisAnimationCall9>(taken[9]);
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
      CuteAxisAnimationCall10 call = reinterpret_cast<CuteAxisAnimationCall10>(taken[10]);
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
      CuteAxisAnimationCall11 call = reinterpret_cast<CuteAxisAnimationCall11>(taken[11]);
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
      CuteAxisAnimationCall12 call = reinterpret_cast<CuteAxisAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  AxisAnimation::~AxisAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN13AxisAnimationD1Ev(AxisAnimation *self) {
  delete self;
}

//  void AxisAnimation::setAnimationType(Animation type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AxisAnimation16setAnimationTypeENS_9AnimationE(
    AxisAnimation *self,
    AxisAnimation::Animation type) {
  self->setAnimationType(type);
}

//  void AxisAnimation::setAnimationPoint(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AxisAnimation17setAnimationPointERK7QPointF(
    AxisAnimation *self,
    const QPointF *point) {
  self->setAnimationPoint(*point);
}

//  QVariant AxisAnimation::interpolated(const QVariant &from, const QVariant
//      &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13AxisAnimation12interpolatedERK8QVariantS2_d(
    const AxisAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(self->interpolated(*from, *to, progress));
}

//  void AxisAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13AxisAnimation18updateCurrentValueERK8QVariant(
    AxisAnimation *self,
    const QVariant *value) {
  self->updateCurrentValue(*value);
}

//  a Python function taken by a CuteAxisAnimation, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AxisAnimation(
    AxisAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteAxisAnimation *>(self)->take(key, call);
}

//  QVariant AxisAnimation::interpolated(const QVariant &from, const QVariant
//      &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK13AxisAnimation12interpolatedERK8QVariantS2_d(
    const AxisAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(
      static_cast<const OwnAxisAnimation *>(self)->OwnAxisAnimation::interpolated(
          *from,
          *to,
          progress));
}

//  void AxisAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13AxisAnimation18updateCurrentValueERK8QVariant(
    AxisAnimation *self,
    const QVariant *value) {
  static_cast<OwnAxisAnimation *>(self)->OwnAxisAnimation::updateCurrentValue(
      *value);
}
