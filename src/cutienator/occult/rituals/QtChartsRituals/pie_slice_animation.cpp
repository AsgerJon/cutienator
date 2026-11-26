//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/piesliceanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/piesliceanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/pieslicedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on PieSliceAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnPieSliceAnimation : PieSliceAnimation {
  using PieSliceAnimation::interpolated;
  using PieSliceAnimation::updateCurrentValue;
};

//  A PieSliceAnimation that Python can take functions over in. Every PieSliceAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef const QVariant * (*CutePieSliceAnimationCall0)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CutePieSliceAnimationCall1)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CutePieSliceAnimationCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CutePieSliceAnimationCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CutePieSliceAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CutePieSliceAnimationCall5)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CutePieSliceAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CutePieSliceAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CutePieSliceAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CutePieSliceAnimation : public PieSliceAnimation {
public:
  using PieSliceAnimation::PieSliceAnimation;
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
  //  QVariant PieSliceAnimation::interpolated(const QVariant &start, const
  //      QVariant &end, qreal progress) const
  QVariant interpolated(
      const QVariant &start,
      const QVariant &end,
      qreal progress) const override {
    if (taken[0]) {
      int handled = 0;
      CutePieSliceAnimationCall0 call = reinterpret_cast<CutePieSliceAnimationCall0>(taken[0]);
      const QVariant * given = call(this, &start, &end, progress, &handled);
      if (handled && given) return *given;
    }
    return PieSliceAnimation::interpolated(start, end, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void PieSliceAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CutePieSliceAnimationCall1 call = reinterpret_cast<CutePieSliceAnimationCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
    PieSliceAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[2]) {
      int handled = 0;
      CutePieSliceAnimationCall2 call = reinterpret_cast<CutePieSliceAnimationCall2>(taken[2]);
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
      CutePieSliceAnimationCall3 call = reinterpret_cast<CutePieSliceAnimationCall3>(taken[3]);
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
      CutePieSliceAnimationCall4 call = reinterpret_cast<CutePieSliceAnimationCall4>(taken[4]);
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
      CutePieSliceAnimationCall5 call = reinterpret_cast<CutePieSliceAnimationCall5>(taken[5]);
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
      CutePieSliceAnimationCall6 call = reinterpret_cast<CutePieSliceAnimationCall6>(taken[6]);
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
      CutePieSliceAnimationCall7 call = reinterpret_cast<CutePieSliceAnimationCall7>(taken[7]);
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
      CutePieSliceAnimationCall8 call = reinterpret_cast<CutePieSliceAnimationCall8>(taken[8]);
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
      CutePieSliceAnimationCall9 call = reinterpret_cast<CutePieSliceAnimationCall9>(taken[9]);
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
      CutePieSliceAnimationCall10 call = reinterpret_cast<CutePieSliceAnimationCall10>(taken[10]);
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
      CutePieSliceAnimationCall11 call = reinterpret_cast<CutePieSliceAnimationCall11>(taken[11]);
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
      CutePieSliceAnimationCall12 call = reinterpret_cast<CutePieSliceAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  PieSliceAnimation::PieSliceAnimation(PieSliceItem *sliceItem)
extern "C" Q_DECL_EXPORT
PieSliceAnimation *ritual_ZN17PieSliceAnimationC1EP12PieSliceItem(
    PieSliceItem *sliceItem) {
  return new CutePieSliceAnimation(sliceItem);
}

//  PieSliceAnimation::~PieSliceAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17PieSliceAnimationD1Ev(PieSliceAnimation *self) {
  delete self;
}

//  void PieSliceAnimation::setValue(const PieSliceData &startValue, const
//      PieSliceData &endValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17PieSliceAnimation8setValueERK12PieSliceDataS2_(
    PieSliceAnimation *self,
    const PieSliceData *startValue,
    const PieSliceData *endValue) {
  self->setValue(*startValue, *endValue);
}

//  void PieSliceAnimation::updateValue(const PieSliceData &endValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17PieSliceAnimation11updateValueERK12PieSliceData(
    PieSliceAnimation *self,
    const PieSliceData *endValue) {
  self->updateValue(*endValue);
}

//  PieSliceData PieSliceAnimation::currentSliceValue()
extern "C" Q_DECL_EXPORT
PieSliceData *ritual_ZN17PieSliceAnimation17currentSliceValueEv(
    PieSliceAnimation *self) {
  return new PieSliceData(self->currentSliceValue());
}

//  QVariant PieSliceAnimation::interpolated(const QVariant &start, const
//      QVariant &end, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17PieSliceAnimation12interpolatedERK8QVariantS2_d(
    const PieSliceAnimation *self,
    const QVariant *start,
    const QVariant *end,
    qreal progress) {
  return new QVariant(self->interpolated(*start, *end, progress));
}

//  void PieSliceAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17PieSliceAnimation18updateCurrentValueERK8QVariant(
    PieSliceAnimation *self,
    const QVariant *value) {
  self->updateCurrentValue(*value);
}

//  a Python function taken by a CutePieSliceAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_PieSliceAnimation(
    PieSliceAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CutePieSliceAnimation *>(self)->take(key, call);
}

//  QVariant PieSliceAnimation::interpolated(const QVariant &start, const
//      QVariant &end, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17PieSliceAnimation12interpolatedERK8QVariantS2_d(
    const PieSliceAnimation *self,
    const QVariant *start,
    const QVariant *end,
    qreal progress) {
  return new QVariant(
      static_cast<const OwnPieSliceAnimation *>(self)->OwnPieSliceAnimation::interpolated(
          *start,
          *end,
          progress));
}

//  void PieSliceAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17PieSliceAnimation18updateCurrentValueERK8QVariant(
    PieSliceAnimation *self,
    const QVariant *value) {
  static_cast<OwnPieSliceAnimation *>(self)->OwnPieSliceAnimation::updateCurrentValue(
      *value);
}

#endif  // QT_CONFIG(charts_pie_chart)
