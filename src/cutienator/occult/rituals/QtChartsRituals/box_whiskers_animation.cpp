//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/boxwhiskersanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/boxwhiskersanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/boxwhiskersdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A BoxWhiskersAnimation that Python can take functions over in. Every BoxWhiskersAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteBoxWhiskersAnimationCall0)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteBoxWhiskersAnimationCall1)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteBoxWhiskersAnimationCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteBoxWhiskersAnimationCall3)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteBoxWhiskersAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteBoxWhiskersAnimationCall5)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteBoxWhiskersAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBoxWhiskersAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBoxWhiskersAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteBoxWhiskersAnimation : public BoxWhiskersAnimation {
public:
  using BoxWhiskersAnimation::BoxWhiskersAnimation;
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
  //  QVariant BoxWhiskersAnimation::interpolated(const QVariant &from,
  //      const QVariant &to, qreal progress) const
  QVariant interpolated(
      const QVariant &from,
      const QVariant &to,
      qreal progress) const override {
    if (taken[0]) {
      int handled = 0;
      CuteBoxWhiskersAnimationCall0 call = reinterpret_cast<CuteBoxWhiskersAnimationCall0>(taken[0]);
      const QVariant * given = call(this, &from, &to, progress, &handled);
      if (handled && given) return *given;
    }
    return BoxWhiskersAnimation::interpolated(from, to, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void BoxWhiskersAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteBoxWhiskersAnimationCall1 call = reinterpret_cast<CuteBoxWhiskersAnimationCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
    BoxWhiskersAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[2]) {
      int handled = 0;
      CuteBoxWhiskersAnimationCall2 call = reinterpret_cast<CuteBoxWhiskersAnimationCall2>(taken[2]);
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
      CuteBoxWhiskersAnimationCall3 call = reinterpret_cast<CuteBoxWhiskersAnimationCall3>(taken[3]);
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
      CuteBoxWhiskersAnimationCall4 call = reinterpret_cast<CuteBoxWhiskersAnimationCall4>(taken[4]);
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
      CuteBoxWhiskersAnimationCall5 call = reinterpret_cast<CuteBoxWhiskersAnimationCall5>(taken[5]);
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
      CuteBoxWhiskersAnimationCall6 call = reinterpret_cast<CuteBoxWhiskersAnimationCall6>(taken[6]);
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
      CuteBoxWhiskersAnimationCall7 call = reinterpret_cast<CuteBoxWhiskersAnimationCall7>(taken[7]);
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
      CuteBoxWhiskersAnimationCall8 call = reinterpret_cast<CuteBoxWhiskersAnimationCall8>(taken[8]);
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
      CuteBoxWhiskersAnimationCall9 call = reinterpret_cast<CuteBoxWhiskersAnimationCall9>(taken[9]);
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
      CuteBoxWhiskersAnimationCall10 call = reinterpret_cast<CuteBoxWhiskersAnimationCall10>(taken[10]);
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
      CuteBoxWhiskersAnimationCall11 call = reinterpret_cast<CuteBoxWhiskersAnimationCall11>(taken[11]);
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
      CuteBoxWhiskersAnimationCall12 call = reinterpret_cast<CuteBoxWhiskersAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *BoxWhiskersAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20BoxWhiskersAnimation10metaObjectEv(
    const BoxWhiskersAnimation *self) {
  return self->metaObject();
}

//  QString BoxWhiskersAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20BoxWhiskersAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(BoxWhiskersAnimation::tr(s, c, n));
}

//  BoxWhiskersAnimation::~BoxWhiskersAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN20BoxWhiskersAnimationD1Ev(BoxWhiskersAnimation *self) {
  delete self;
}

//  QVariant BoxWhiskersAnimation::interpolated(const QVariant &from, const
//      QVariant &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20BoxWhiskersAnimation12interpolatedERK8QVariantS2_d(
    const BoxWhiskersAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(self->interpolated(*from, *to, progress));
}

//  void BoxWhiskersAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20BoxWhiskersAnimation18updateCurrentValueERK8QVariant(
    BoxWhiskersAnimation *self,
    const QVariant *value) {
  self->updateCurrentValue(*value);
}

//  void BoxWhiskersAnimation::setup(const BoxWhiskersData &startData, const
//      BoxWhiskersData &endData)
extern "C" Q_DECL_EXPORT
void ritual_ZN20BoxWhiskersAnimation5setupERK15BoxWhiskersDataS2_(
    BoxWhiskersAnimation *self,
    const BoxWhiskersData *startData,
    const BoxWhiskersData *endData) {
  self->setup(*startData, *endData);
}

//  void BoxWhiskersAnimation::setEndData(const BoxWhiskersData &endData)
extern "C" Q_DECL_EXPORT
void ritual_ZN20BoxWhiskersAnimation10setEndDataERK15BoxWhiskersData(
    BoxWhiskersAnimation *self,
    const BoxWhiskersData *endData) {
  self->setEndData(*endData);
}

//  void BoxWhiskersAnimation::setStartData(const BoxWhiskersData &endData)
extern "C" Q_DECL_EXPORT
void ritual_ZN20BoxWhiskersAnimation12setStartDataERK15BoxWhiskersData(
    BoxWhiskersAnimation *self,
    const BoxWhiskersData *endData) {
  self->setStartData(*endData);
}

//  a Python function taken by a CuteBoxWhiskersAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_BoxWhiskersAnimation(
    BoxWhiskersAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteBoxWhiskersAnimation *>(self)->take(key, call);
}

//  QVariant BoxWhiskersAnimation::interpolated(const QVariant &from, const
//      QVariant &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20BoxWhiskersAnimation12interpolatedERK8QVariantS2_d(
    const BoxWhiskersAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(
      self->BoxWhiskersAnimation::interpolated(
          *from,
          *to,
          progress));
}

//  void BoxWhiskersAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20BoxWhiskersAnimation18updateCurrentValueERK8QVariant(
    BoxWhiskersAnimation *self,
    const QVariant *value) {
  self->BoxWhiskersAnimation::updateCurrentValue(*value);
}

#endif  // QT_CONFIG(charts_boxplot_chart)
