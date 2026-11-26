//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#if QT_CONFIG(easingcurve)
#include <QtCore/qeasingcurve.h>
#endif
#include <QtCore/qdebug.h>
#include <cstring>

//  Only a class built on QQuickAnimatorJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAnimatorJob : QQuickAnimatorJob {
  using QQuickAnimatorJob::debugAnimation;
};

//  A QQuickAnimatorJob that Python can take functions over in. Every QQuickAnimatorJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAnimatorJobCall0)(const void *, QQuickItem *, int *);
#if QT_CONFIG(qml_animation)
typedef int (*CuteQQuickAnimatorJobCall1)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorJobCall2)(const void *, QQuickAnimatorController *, int *);
typedef void (*CuteQQuickAnimatorJobCall3)(const void *, int *);
typedef void (*CuteQQuickAnimatorJobCall4)(const void *, int *);
typedef void (*CuteQQuickAnimatorJobCall5)(const void *, int *);
typedef void (*CuteQQuickAnimatorJobCall6)(const void *, int *);
typedef void (*CuteQQuickAnimatorJobCall7)(const void *, int *);
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorJobCall8)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorJobCall9)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorJobCall10)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorJobCall11)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorJobCall12)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorJobCall13)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickAnimatorJob : public QQuickAnimatorJob {
public:
  using QQuickAnimatorJob::QQuickAnimatorJob;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob9setTargetEP10QQuickItem")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob8durationEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob10initializeEP24QQuickAnimatorController")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob10invalidateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob9writeBackEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob7preSyncEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob8postSyncEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob6commitEv")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob17updateCurrentTimeEi")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateLoopCountEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

  //  void QQuickAnimatorJob::setTarget(QQuickItem *target)
  void setTarget(QQuickItem *target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall0 call = reinterpret_cast<CuteQQuickAnimatorJobCall0>(taken[0]);
      call(this, target, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::setTarget(target);
  }

#if QT_CONFIG(qml_animation)
  //  int QQuickAnimatorJob::duration() const
  int duration() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall1 call = reinterpret_cast<CuteQQuickAnimatorJobCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAnimatorJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

  //  void QQuickAnimatorJob::initialize(QQuickAnimatorController
  //      *controller)
  void initialize(QQuickAnimatorController *controller) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall2 call = reinterpret_cast<CuteQQuickAnimatorJobCall2>(taken[2]);
      call(this, controller, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::initialize(controller);
  }

  //  void QQuickAnimatorJob::invalidate()
  void invalidate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall3 call = reinterpret_cast<CuteQQuickAnimatorJobCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAnimatorJob::writeBack()
  void writeBack() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall4 call = reinterpret_cast<CuteQQuickAnimatorJobCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAnimatorJob::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall5 call = reinterpret_cast<CuteQQuickAnimatorJobCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::preSync();
  }

  //  void QQuickAnimatorJob::postSync()
  void postSync() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall6 call = reinterpret_cast<CuteQQuickAnimatorJobCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::postSync();
  }

  //  void QQuickAnimatorJob::commit()
  void commit() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall7 call = reinterpret_cast<CuteQQuickAnimatorJobCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::commit();
  }

#if QT_CONFIG(qml_animation)
  //  void QQuickAnimatorJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall8 call = reinterpret_cast<CuteQQuickAnimatorJobCall8>(taken[8]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall9 call = reinterpret_cast<CuteQQuickAnimatorJobCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall10 call = reinterpret_cast<CuteQQuickAnimatorJobCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateLoopCount(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateState(QAbstractAnimationJob::State
  //      newState, QAbstractAnimationJob::State oldState)
  void updateState(
      QAbstractAnimationJob::State newState,
      QAbstractAnimationJob::State oldState) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall11 call = reinterpret_cast<CuteQQuickAnimatorJobCall11>(taken[11]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateDirection(QAbstractAnimationJob::Di
  //      rection direction)
  void updateDirection(QAbstractAnimationJob::Direction direction) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall12 call = reinterpret_cast<CuteQQuickAnimatorJobCall12>(taken[12]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::topLevelAnimationLoopChanged()
  void topLevelAnimationLoopChanged() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAnimatorJobCall13 call = reinterpret_cast<CuteQQuickAnimatorJobCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)
};

//  void QQuickAnimatorJob::setTarget(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob9setTargetEP10QQuickItem(
    QQuickAnimatorJob *self,
    QQuickItem *target) {
  self->setTarget(target);
}

//  QQuickItem *QQuickAnimatorJob::target() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK17QQuickAnimatorJob6targetEv(
    const QQuickAnimatorJob *self) {
  return self->target();
}

//  void QQuickAnimatorJob::setFrom(qreal from)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob7setFromEd(
    QQuickAnimatorJob *self,
    qreal from) {
  self->setFrom(from);
}

//  qreal QQuickAnimatorJob::from() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickAnimatorJob4fromEv(const QQuickAnimatorJob *self) {
  return self->from();
}

//  void QQuickAnimatorJob::setTo(qreal to)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob5setToEd(
    QQuickAnimatorJob *self,
    qreal to) {
  self->setTo(to);
}

//  qreal QQuickAnimatorJob::to() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickAnimatorJob2toEv(const QQuickAnimatorJob *self) {
  return self->to();
}

//  void QQuickAnimatorJob::setDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob11setDurationEi(
    QQuickAnimatorJob *self,
    int duration) {
  self->setDuration(duration);
}

//  int QQuickAnimatorJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickAnimatorJob8durationEv(const QQuickAnimatorJob *self) {
  return self->duration();
}

//  QEasingCurve QQuickAnimatorJob::easingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK17QQuickAnimatorJob11easingCurveEv(
    const QQuickAnimatorJob *self) {
  return new QEasingCurve(self->easingCurve());
}

//  void QQuickAnimatorJob::setEasingCurve(const QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob14setEasingCurveERK12QEasingCurve(
    QQuickAnimatorJob *self,
    const QEasingCurve *curve) {
  self->setEasingCurve(*curve);
}

//  void QQuickAnimatorJob::initialize(QQuickAnimatorController *controller)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob10initializeEP24QQuickAnimatorController(
    QQuickAnimatorJob *self,
    QQuickAnimatorController *controller) {
  self->initialize(controller);
}

//  void QQuickAnimatorJob::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob10invalidateEv(QQuickAnimatorJob *self) {
  self->invalidate();
}

//  void QQuickAnimatorJob::writeBack()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob9writeBackEv(QQuickAnimatorJob *self) {
  self->writeBack();
}

//  void QQuickAnimatorJob::preSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob7preSyncEv(QQuickAnimatorJob *self) {
  self->preSync();
}

//  void QQuickAnimatorJob::postSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob8postSyncEv(QQuickAnimatorJob *self) {
  self->postSync();
}

//  void QQuickAnimatorJob::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob6commitEv(QQuickAnimatorJob *self) {
  self->commit();
}

//  bool QQuickAnimatorJob::isTransform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickAnimatorJob11isTransformEv(
    const QQuickAnimatorJob *self) {
  return self->isTransform();
}

//  bool QQuickAnimatorJob::isUniform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickAnimatorJob9isUniformEv(
    const QQuickAnimatorJob *self) {
  return self->isUniform();
}

//  qreal QQuickAnimatorJob::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickAnimatorJob5valueEv(const QQuickAnimatorJob *self) {
  return self->value();
}

//  QQuickAnimatorController *QQuickAnimatorJob::controller() const
extern "C" Q_DECL_EXPORT
QQuickAnimatorController *ritual_ZNK17QQuickAnimatorJob10controllerEv(
    const QQuickAnimatorJob *self) {
  return self->controller();
}

//  QQuickAnimatorJob::QQuickAnimatorJob()
extern "C" Q_DECL_EXPORT
QQuickAnimatorJob *ritual_ZN17QQuickAnimatorJobC1Ev() {
  return new CuteQQuickAnimatorJob();
}

//  void QQuickAnimatorJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QQuickAnimatorJob14debugAnimationE6QDebug(
    const QQuickAnimatorJob *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  qreal QQuickAnimatorJob::progress(int time) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickAnimatorJob8progressEi(
    const QQuickAnimatorJob *self,
    int time) {
  return self->progress(time);
}

//  void QQuickAnimatorJob::boundValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAnimatorJob10boundValueEv(QQuickAnimatorJob *self) {
  self->boundValue();
}

//  a Python function taken by a CuteQQuickAnimatorJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimatorJob(
    QQuickAnimatorJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimatorJob *>(self)->take(key, call);
}

//  void QQuickAnimatorJob::setTarget(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickAnimatorJob9setTargetEP10QQuickItem(
    QQuickAnimatorJob *self,
    QQuickItem *target) {
  self->QQuickAnimatorJob::setTarget(target);
}

//  int QQuickAnimatorJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QQuickAnimatorJob8durationEv(
    const QQuickAnimatorJob *self) {
  return self->QQuickAnimatorJob::duration();
}

//  void QQuickAnimatorJob::initialize(QQuickAnimatorController *controller)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickAnimatorJob10initializeEP24QQuickAnimatorController(
    QQuickAnimatorJob *self,
    QQuickAnimatorController *controller) {
  self->QQuickAnimatorJob::initialize(controller);
}

//  void QQuickAnimatorJob::preSync()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickAnimatorJob7preSyncEv(QQuickAnimatorJob *self) {
  self->QQuickAnimatorJob::preSync();
}

//  void QQuickAnimatorJob::postSync()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickAnimatorJob8postSyncEv(QQuickAnimatorJob *self) {
  self->QQuickAnimatorJob::postSync();
}

//  void QQuickAnimatorJob::commit()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickAnimatorJob6commitEv(QQuickAnimatorJob *self) {
  self->QQuickAnimatorJob::commit();
}

//  void QQuickAnimatorJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK17QQuickAnimatorJob14debugAnimationE6QDebug(
    const QQuickAnimatorJob *self,
    const QDebug *d) {
  static_cast<const OwnQQuickAnimatorJob *>(self)->OwnQQuickAnimatorJob::debugAnimation(
      *d);
}
