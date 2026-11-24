//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/candlestickbodywicksanimation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/candlestickbodywicksanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/candlestickdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A CandlestickBodyWicksAnimation that Python can take functions over in. Every CandlestickBodyWicksAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef void (*CuteCandlestickBodyWicksAnimationCall0)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteCandlestickBodyWicksAnimationCall1)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteCandlestickBodyWicksAnimationCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteCandlestickBodyWicksAnimationCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteCandlestickBodyWicksAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteCandlestickBodyWicksAnimationCall5)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteCandlestickBodyWicksAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteCandlestickBodyWicksAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickBodyWicksAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickBodyWicksAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickBodyWicksAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickBodyWicksAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteCandlestickBodyWicksAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteCandlestickBodyWicksAnimation : public CandlestickBodyWicksAnimation {
public:
  using CandlestickBodyWicksAnimation::CandlestickBodyWicksAnimation;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN17QVariantAnimation18updateCurrentValueERK8QVariant")) {
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
  //  void CandlestickBodyWicksAnimation::updateCurrentValue(const QVariant
  //      &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteCandlestickBodyWicksAnimationCall0 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall0>(taken[0]);
      call(this, &value, &handled);
      if (handled) return;
    }
    CandlestickBodyWicksAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  QVariant CandlestickBodyWicksAnimation::interpolated(const QVariant
  //      &from, const QVariant &to, qreal progress) const
  QVariant interpolated(
      const QVariant &from,
      const QVariant &to,
      qreal progress) const override {
    if (taken[1]) {
      int handled = 0;
      CuteCandlestickBodyWicksAnimationCall1 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall1>(taken[1]);
      const QVariant * given = call(this, &from, &to, progress, &handled);
      if (handled && given) return *given;
    }
    return CandlestickBodyWicksAnimation::interpolated(from, to, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[2]) {
      int handled = 0;
      CuteCandlestickBodyWicksAnimationCall2 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall2>(taken[2]);
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
      CuteCandlestickBodyWicksAnimationCall3 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall3>(taken[3]);
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
      CuteCandlestickBodyWicksAnimationCall4 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall4>(taken[4]);
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
      CuteCandlestickBodyWicksAnimationCall5 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall5>(taken[5]);
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
      CuteCandlestickBodyWicksAnimationCall6 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall6>(taken[6]);
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
      CuteCandlestickBodyWicksAnimationCall7 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall7>(taken[7]);
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
      CuteCandlestickBodyWicksAnimationCall8 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall8>(taken[8]);
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
      CuteCandlestickBodyWicksAnimationCall9 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall9>(taken[9]);
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
      CuteCandlestickBodyWicksAnimationCall10 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall10>(taken[10]);
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
      CuteCandlestickBodyWicksAnimationCall11 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall11>(taken[11]);
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
      CuteCandlestickBodyWicksAnimationCall12 call = reinterpret_cast<CuteCandlestickBodyWicksAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *CandlestickBodyWicksAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29CandlestickBodyWicksAnimation10metaObjectEv(
    const CandlestickBodyWicksAnimation *self) {
  return self->metaObject();
}

//  QString CandlestickBodyWicksAnimation::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29CandlestickBodyWicksAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(CandlestickBodyWicksAnimation::tr(s, c, n));
}

//  CandlestickBodyWicksAnimation::~CandlestickBodyWicksAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN29CandlestickBodyWicksAnimationD1Ev(
    CandlestickBodyWicksAnimation *self) {
  delete self;
}

//  void CandlestickBodyWicksAnimation::setup(const CandlestickData
//      &startData, const CandlestickData &endData)
extern "C" Q_DECL_EXPORT
void ritual_ZN29CandlestickBodyWicksAnimation5setupERK15CandlestickDataS2_(
    CandlestickBodyWicksAnimation *self,
    const CandlestickData *startData,
    const CandlestickData *endData) {
  self->setup(*startData, *endData);
}

//  void CandlestickBodyWicksAnimation::setStartData(const CandlestickData
//      &startData)
extern "C" Q_DECL_EXPORT
void ritual_ZN29CandlestickBodyWicksAnimation12setStartDataERK15CandlestickData(
    CandlestickBodyWicksAnimation *self,
    const CandlestickData *startData) {
  self->setStartData(*startData);
}

//  void CandlestickBodyWicksAnimation::setEndData(const CandlestickData
//      &endData)
extern "C" Q_DECL_EXPORT
void ritual_ZN29CandlestickBodyWicksAnimation10setEndDataERK15CandlestickData(
    CandlestickBodyWicksAnimation *self,
    const CandlestickData *endData) {
  self->setEndData(*endData);
}

//  void CandlestickBodyWicksAnimation::updateCurrentValue(const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN29CandlestickBodyWicksAnimation18updateCurrentValueERK8QVariant(
    CandlestickBodyWicksAnimation *self,
    const QVariant *value) {
  self->updateCurrentValue(*value);
}

//  QVariant CandlestickBodyWicksAnimation::interpolated(const QVariant
//      &from, const QVariant &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK29CandlestickBodyWicksAnimation12interpolatedERK8QVariantS2_d(
    const CandlestickBodyWicksAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(self->interpolated(*from, *to, progress));
}

//  a Python function taken by a CuteCandlestickBodyWicksAnimation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_CandlestickBodyWicksAnimation(
    CandlestickBodyWicksAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteCandlestickBodyWicksAnimation *>(self)->take(key, call);
}

//  void CandlestickBodyWicksAnimation::updateCurrentValue(const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29CandlestickBodyWicksAnimation18updateCurrentValueERK8QVariant(
    CandlestickBodyWicksAnimation *self,
    const QVariant *value) {
  self->CandlestickBodyWicksAnimation::updateCurrentValue(*value);
}

//  QVariant CandlestickBodyWicksAnimation::interpolated(const QVariant
//      &from, const QVariant &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK29CandlestickBodyWicksAnimation12interpolatedERK8QVariantS2_d(
    const CandlestickBodyWicksAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(
      self->CandlestickBodyWicksAnimation::interpolated(
          *from,
          *to,
          progress));
}
