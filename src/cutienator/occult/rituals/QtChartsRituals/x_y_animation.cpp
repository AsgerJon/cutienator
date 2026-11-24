//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/xyanimation_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/xyanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on XYAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnXYAnimation : XYAnimation {
  using XYAnimation::interpolated;
  using XYAnimation::updateCurrentValue;
  using XYAnimation::updateState;
};

//  A XYAnimation that Python can take functions over in. Every XYAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteXYAnimationCall0)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteXYAnimationCall1)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteXYAnimationCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef int (*CuteXYAnimationCall3)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteXYAnimationCall4)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteXYAnimationCall5)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteXYAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteXYAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteXYAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteXYAnimation : public XYAnimation {
public:
  using XYAnimation::XYAnimation;
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
  //  QVariant XYAnimation::interpolated(const QVariant &start, const
  //      QVariant &end, qreal progress) const
  QVariant interpolated(
      const QVariant &start,
      const QVariant &end,
      qreal progress) const override {
    if (taken[0]) {
      int handled = 0;
      CuteXYAnimationCall0 call = reinterpret_cast<CuteXYAnimationCall0>(taken[0]);
      const QVariant * given = call(this, &start, &end, progress, &handled);
      if (handled && given) return *given;
    }
    return XYAnimation::interpolated(start, end, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void XYAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteXYAnimationCall1 call = reinterpret_cast<CuteXYAnimationCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
    XYAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void XYAnimation::updateState(QAbstractAnimation::State newState,
  //      QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[2]) {
      int handled = 0;
      CuteXYAnimationCall2 call = reinterpret_cast<CuteXYAnimationCall2>(taken[2]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    XYAnimation::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[3]) {
      int handled = 0;
      CuteXYAnimationCall3 call = reinterpret_cast<CuteXYAnimationCall3>(taken[3]);
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
      CuteXYAnimationCall4 call = reinterpret_cast<CuteXYAnimationCall4>(taken[4]);
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
      CuteXYAnimationCall5 call = reinterpret_cast<CuteXYAnimationCall5>(taken[5]);
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
      CuteXYAnimationCall6 call = reinterpret_cast<CuteXYAnimationCall6>(taken[6]);
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
      CuteXYAnimationCall7 call = reinterpret_cast<CuteXYAnimationCall7>(taken[7]);
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
      CuteXYAnimationCall8 call = reinterpret_cast<CuteXYAnimationCall8>(taken[8]);
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
      CuteXYAnimationCall9 call = reinterpret_cast<CuteXYAnimationCall9>(taken[9]);
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
      CuteXYAnimationCall10 call = reinterpret_cast<CuteXYAnimationCall10>(taken[10]);
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
      CuteXYAnimationCall11 call = reinterpret_cast<CuteXYAnimationCall11>(taken[11]);
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
      CuteXYAnimationCall12 call = reinterpret_cast<CuteXYAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  XYAnimation::~XYAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN11XYAnimationD1Ev(XYAnimation *self) {
  delete self;
}

//  void XYAnimation::setup(const QList<QPointF> &oldPoints, const
//      QList<QPointF> &newPoints, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN11XYAnimation5setupERK5QListI7QPointFES4_i(
    XYAnimation *self,
    const QList<QPointF> *oldPoints,
    const QList<QPointF> *newPoints,
    int index) {
  self->setup(*oldPoints, *newPoints, index);
}

//  Animation XYAnimation::animationType() const
extern "C" Q_DECL_EXPORT
XYAnimation::Animation ritual_ZNK11XYAnimation13animationTypeEv(
    const XYAnimation *self) {
  return self->animationType();
}

//  QVariant XYAnimation::interpolated(const QVariant &start, const QVariant
//      &end, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11XYAnimation12interpolatedERK8QVariantS2_d(
    const XYAnimation *self,
    const QVariant *start,
    const QVariant *end,
    qreal progress) {
  return new QVariant(self->interpolated(*start, *end, progress));
}

//  void XYAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11XYAnimation18updateCurrentValueERK8QVariant(
    XYAnimation *self,
    const QVariant *value) {
  self->updateCurrentValue(*value);
}

//  void XYAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN11XYAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    XYAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  self->updateState(newState, oldState);
}

//  XYChart *XYAnimation::chartItem()
extern "C" Q_DECL_EXPORT
XYChart *ritual_ZN11XYAnimation9chartItemEv(XYAnimation *self) {
  return self->chartItem();
}

//  a Python function taken by a CuteXYAnimation, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_XYAnimation(
    XYAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteXYAnimation *>(self)->take(key, call);
}

//  QVariant XYAnimation::interpolated(const QVariant &start, const QVariant
//      &end, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK11XYAnimation12interpolatedERK8QVariantS2_d(
    const XYAnimation *self,
    const QVariant *start,
    const QVariant *end,
    qreal progress) {
  return new QVariant(
      static_cast<const OwnXYAnimation *>(self)->OwnXYAnimation::interpolated(
          *start,
          *end,
          progress));
}

//  void XYAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11XYAnimation18updateCurrentValueERK8QVariant(
    XYAnimation *self,
    const QVariant *value) {
  static_cast<OwnXYAnimation *>(self)->OwnXYAnimation::updateCurrentValue(
      *value);
}

//  void XYAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11XYAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    XYAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  static_cast<OwnXYAnimation *>(self)->OwnXYAnimation::updateState(
      newState,
      oldState);
}
