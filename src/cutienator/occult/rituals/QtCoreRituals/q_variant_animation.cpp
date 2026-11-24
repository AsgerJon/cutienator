//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariantanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(animation)
#if QT_CONFIG(animation)
#include <QtCore/qvariantanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qeasingcurve.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QVariantAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQVariantAnimation : QVariantAnimation {
  using QVariantAnimation::event;
  using QVariantAnimation::updateCurrentTime;
  using QVariantAnimation::updateState;
  using QVariantAnimation::updateCurrentValue;
  using QVariantAnimation::interpolated;
};

//  A QVariantAnimation that Python can take functions over in. Every QVariantAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef int (*CuteQVariantAnimationCall0)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQVariantAnimationCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQVariantAnimationCall2)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQVariantAnimationCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQVariantAnimationCall4)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef const QVariant * (*CuteQVariantAnimationCall5)(const void *, const QVariant *, const QVariant *, qreal, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQVariantAnimationCall6)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVariantAnimationCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVariantAnimationCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVariantAnimationCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVariantAnimationCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVariantAnimationCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVariantAnimationCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVariantAnimation : public QVariantAnimation {
public:
  using QVariantAnimation::QVariantAnimation;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK18QAbstractAnimation8durationEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation17updateCurrentTimeEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation11updateStateENS_5StateES0_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN17QVariantAnimation18updateCurrentValueERK8QVariant")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d")) {
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
  //  int QVariantAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQVariantAnimationCall0 call = reinterpret_cast<CuteQVariantAnimationCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQVariantAnimationCall1 call = reinterpret_cast<CuteQVariantAnimationCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQVariantAnimationCall2 call = reinterpret_cast<CuteQVariantAnimationCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQVariantAnimationCall3 call = reinterpret_cast<CuteQVariantAnimationCall3>(taken[3]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QVariantAnimation::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QVariantAnimation::updateCurrentValue(const QVariant &value)
  void updateCurrentValue(const QVariant &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQVariantAnimationCall4 call = reinterpret_cast<CuteQVariantAnimationCall4>(taken[4]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QVariantAnimation::updateCurrentValue(value);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  QVariant QVariantAnimation::interpolated(const QVariant &from, const
  //      QVariant &to, qreal progress) const
  QVariant interpolated(
      const QVariant &from,
      const QVariant &to,
      qreal progress) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQVariantAnimationCall5 call = reinterpret_cast<CuteQVariantAnimationCall5>(taken[5]);
      const QVariant * given = call(this, &from, &to, progress, &handled);
      if (handled && given) return *given;
    }
    return QVariantAnimation::interpolated(from, to, progress);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void
  //      QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
  //      direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[6]) {
      int handled = 0;
      CuteQVariantAnimationCall6 call = reinterpret_cast<CuteQVariantAnimationCall6>(taken[6]);
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
      CuteQVariantAnimationCall7 call = reinterpret_cast<CuteQVariantAnimationCall7>(taken[7]);
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
      CuteQVariantAnimationCall8 call = reinterpret_cast<CuteQVariantAnimationCall8>(taken[8]);
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
      CuteQVariantAnimationCall9 call = reinterpret_cast<CuteQVariantAnimationCall9>(taken[9]);
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
      CuteQVariantAnimationCall10 call = reinterpret_cast<CuteQVariantAnimationCall10>(taken[10]);
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
      CuteQVariantAnimationCall11 call = reinterpret_cast<CuteQVariantAnimationCall11>(taken[11]);
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
      CuteQVariantAnimationCall12 call = reinterpret_cast<CuteQVariantAnimationCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVariantAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QVariantAnimation10metaObjectEv(
    const QVariantAnimation *self) {
  return self->metaObject();
}

//  QString QVariantAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QVariantAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVariantAnimation::tr(s, c, n));
}

//  QVariantAnimation::QVariantAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QVariantAnimation *ritual_ZN17QVariantAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQVariantAnimation(parent);
}

//  QVariantAnimation::~QVariantAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimationD1Ev(QVariantAnimation *self) {
  delete self;
}

//  QVariant QVariantAnimation::startValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QVariantAnimation10startValueEv(
    const QVariantAnimation *self) {
  return new QVariant(self->startValue());
}

//  void QVariantAnimation::setStartValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation13setStartValueERK8QVariant(
    QVariantAnimation *self,
    const QVariant *value) {
  self->setStartValue(*value);
}

//  QVariant QVariantAnimation::endValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QVariantAnimation8endValueEv(
    const QVariantAnimation *self) {
  return new QVariant(self->endValue());
}

//  void QVariantAnimation::setEndValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation11setEndValueERK8QVariant(
    QVariantAnimation *self,
    const QVariant *value) {
  self->setEndValue(*value);
}

//  QVariant QVariantAnimation::keyValueAt(qreal step) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QVariantAnimation10keyValueAtEd(
    const QVariantAnimation *self,
    qreal step) {
  return new QVariant(self->keyValueAt(step));
}

//  void QVariantAnimation::setKeyValueAt(qreal step, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation13setKeyValueAtEdRK8QVariant(
    QVariantAnimation *self,
    qreal step,
    const QVariant *value) {
  self->setKeyValueAt(step, *value);
}

//  QVariant QVariantAnimation::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QVariantAnimation12currentValueEv(
    const QVariantAnimation *self) {
  return new QVariant(self->currentValue());
}

//  int QVariantAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QVariantAnimation8durationEv(const QVariantAnimation *self) {
  return self->duration();
}

//  void QVariantAnimation::setDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation11setDurationEi(
    QVariantAnimation *self,
    int msecs) {
  self->setDuration(msecs);
}

//  QEasingCurve QVariantAnimation::easingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK17QVariantAnimation11easingCurveEv(
    const QVariantAnimation *self) {
  return new QEasingCurve(self->easingCurve());
}

//  void QVariantAnimation::setEasingCurve(const QEasingCurve &easing)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation14setEasingCurveERK12QEasingCurve(
    QVariantAnimation *self,
    const QEasingCurve *easing) {
  self->setEasingCurve(*easing);
}

//  bool QVariantAnimation::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QVariantAnimation5eventEP6QEvent(
    QVariantAnimation *self,
    QEvent *event) {
  return self->event(event);
}

//  void QVariantAnimation::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation17updateCurrentTimeEi(
    QVariantAnimation *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  void QVariantAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    QVariantAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  self->updateState(newState, oldState);
}

//  void QVariantAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVariantAnimation18updateCurrentValueERK8QVariant(
    QVariantAnimation *self,
    const QVariant *value) {
  self->updateCurrentValue(*value);
}

//  QVariant QVariantAnimation::interpolated(const QVariant &from, const
//      QVariant &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d(
    const QVariantAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(self->interpolated(*from, *to, progress));
}

//  QVariantAnimationPrivate *QVariantAnimation::d_func()
extern "C" Q_DECL_EXPORT
QVariantAnimationPrivate *ritual_ZN17QVariantAnimation6d_funcEv(
    QVariantAnimation *self) {
  return self->d_func();
}

//  const QVariantAnimationPrivate *QVariantAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const QVariantAnimationPrivate *ritual_ZNK17QVariantAnimation6d_funcEv(
    const QVariantAnimation *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQVariantAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVariantAnimation(
    QVariantAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVariantAnimation *>(self)->take(key, call);
}

//  int QVariantAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QVariantAnimation8durationEv(
    const QVariantAnimation *self) {
  return self->QVariantAnimation::duration();
}

//  bool QVariantAnimation::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QVariantAnimation5eventEP6QEvent(
    QVariantAnimation *self,
    QEvent *event) {
  return static_cast<OwnQVariantAnimation *>(self)->OwnQVariantAnimation::event(
      event);
}

//  void QVariantAnimation::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QVariantAnimation17updateCurrentTimeEi(
    QVariantAnimation *self,
    int a0) {
  static_cast<OwnQVariantAnimation *>(self)->OwnQVariantAnimation::updateCurrentTime(
      a0);
}

//  void QVariantAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QVariantAnimation11updateStateEN18QAbstractAnimation5StateES1_(
    QVariantAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  static_cast<OwnQVariantAnimation *>(self)->OwnQVariantAnimation::updateState(
      newState,
      oldState);
}

//  void QVariantAnimation::updateCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QVariantAnimation18updateCurrentValueERK8QVariant(
    QVariantAnimation *self,
    const QVariant *value) {
  static_cast<OwnQVariantAnimation *>(self)->OwnQVariantAnimation::updateCurrentValue(
      *value);
}

//  QVariant QVariantAnimation::interpolated(const QVariant &from, const
//      QVariant &to, qreal progress) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QVariantAnimation12interpolatedERK8QVariantS2_d(
    const QVariantAnimation *self,
    const QVariant *from,
    const QVariant *to,
    qreal progress) {
  return new QVariant(
      static_cast<const OwnQVariantAnimation *>(self)->OwnQVariantAnimation::interpolated(
          *from,
          *to,
          progress));
}

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(animation)
