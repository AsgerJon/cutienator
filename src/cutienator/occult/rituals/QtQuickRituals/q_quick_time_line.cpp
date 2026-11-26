//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktimeline_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25:
//  took out the ritual of QQuickTimeLine::sync(), which
//  Qt declares but its library does not offer (undefined
//  reference when linking), and its row.
//  Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktimeline_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qeasingcurve.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickTimeLine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTimeLine : QQuickTimeLine {
  using QQuickTimeLine::updateCurrentTime;
  using QQuickTimeLine::debugAnimation;
};

//  A QQuickTimeLine that Python can take functions over in. Every QQuickTimeLine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQQuickTimeLineCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTimeLineCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTimeLineCall2)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTimeLineCall3)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTimeLineCall4)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTimeLineCall5)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTimeLineCall6)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTimeLineCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTimeLineCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimeLineCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimeLineCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimeLineCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimeLineCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTimeLineCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTimeLine : public QQuickTimeLine {
public:
  using QQuickTimeLine::QQuickTimeLine;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob8durationEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob17updateCurrentTimeEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateLoopCountEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  int QQuickTimeLine::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTimeLineCall0 call = reinterpret_cast<CuteQQuickTimeLineCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTimeLine::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickTimeLine::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTimeLineCall1 call = reinterpret_cast<CuteQQuickTimeLineCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickTimeLine::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickTimeLine::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTimeLineCall2 call = reinterpret_cast<CuteQQuickTimeLineCall2>(taken[2]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QQuickTimeLine::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTimeLineCall3 call = reinterpret_cast<CuteQQuickTimeLineCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTimeLineCall4 call = reinterpret_cast<CuteQQuickTimeLineCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTimeLineCall5 call = reinterpret_cast<CuteQQuickTimeLineCall5>(taken[5]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::topLevelAnimationLoopChanged()
  void topLevelAnimationLoopChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTimeLineCall6 call = reinterpret_cast<CuteQQuickTimeLineCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTimeLineCall7 call = reinterpret_cast<CuteQQuickTimeLineCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTimeLineCall8 call = reinterpret_cast<CuteQQuickTimeLineCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTimeLineCall9 call = reinterpret_cast<CuteQQuickTimeLineCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTimeLineCall10 call = reinterpret_cast<CuteQQuickTimeLineCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTimeLineCall11 call = reinterpret_cast<CuteQQuickTimeLineCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTimeLineCall12 call = reinterpret_cast<CuteQQuickTimeLineCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTimeLineCall13 call = reinterpret_cast<CuteQQuickTimeLineCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTimeLine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickTimeLine10metaObjectEv(
    const QQuickTimeLine *self) {
  return self->metaObject();
}

//  void *QQuickTimeLine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickTimeLine11qt_metacastEPKc(
    QQuickTimeLine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QQuickTimeLine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickTimeLine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTimeLine::tr(s, c, n));
}

//  QQuickTimeLine::QQuickTimeLine(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTimeLine *ritual_ZN14QQuickTimeLineC1EP7QObject(QObject *parent) {
  return new CuteQQuickTimeLine(parent);
}

//  QQuickTimeLine::~QQuickTimeLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLineD1Ev(QQuickTimeLine *self) {
  delete self;
}

//  SyncMode QQuickTimeLine::syncMode() const
extern "C" Q_DECL_EXPORT
QQuickTimeLine::SyncMode ritual_ZNK14QQuickTimeLine8syncModeEv(
    const QQuickTimeLine *self) {
  return self->syncMode();
}

//  void QQuickTimeLine::setSyncMode(SyncMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine11setSyncModeENS_8SyncModeE(
    QQuickTimeLine *self,
    QQuickTimeLine::SyncMode a0) {
  self->setSyncMode(a0);
}

//  void QQuickTimeLine::pause(QQuickTimeLineObject &a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine5pauseER20QQuickTimeLineObjecti(
    QQuickTimeLine *self,
    QQuickTimeLineObject *a0,
    int a1) {
  self->pause(*a0, a1);
}

//  void QQuickTimeLine::callback(const QQuickTimeLineCallback &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine8callbackERK22QQuickTimeLineCallback(
    QQuickTimeLine *self,
    const QQuickTimeLineCallback *a0) {
  self->callback(*a0);
}

//  void QQuickTimeLine::set(QQuickTimeLineValue &a0, qreal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine3setER19QQuickTimeLineValued(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0,
    qreal a1) {
  self->set(*a0, a1);
}

//  int QQuickTimeLine::accel(QQuickTimeLineValue &a0, qreal velocity, qreal
//      accel)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTimeLine5accelER19QQuickTimeLineValuedd(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0,
    qreal velocity,
    qreal accel) {
  return self->accel(*a0, velocity, accel);
}

//  int QQuickTimeLine::accel(QQuickTimeLineValue &a0, qreal velocity, qreal
//      accel, qreal maxDistance)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTimeLine5accelER19QQuickTimeLineValueddd(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0,
    qreal velocity,
    qreal accel,
    qreal maxDistance) {
  return self->accel(*a0, velocity, accel, maxDistance);
}

//  int QQuickTimeLine::accelDistance(QQuickTimeLineValue &a0, qreal
//      velocity, qreal distance)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTimeLine13accelDistanceER19QQuickTimeLineValuedd(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0,
    qreal velocity,
    qreal distance) {
  return self->accelDistance(*a0, velocity, distance);
}

//  void QQuickTimeLine::move(QQuickTimeLineValue &a0, qreal destination, int
//      time)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine4moveER19QQuickTimeLineValuedi(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0,
    qreal destination,
    int time) {
  self->move(*a0, destination, time);
}

//  void QQuickTimeLine::move(QQuickTimeLineValue &a0, qreal destination,
//      const QEasingCurve &a2, int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine4moveER19QQuickTimeLineValuedRK12QEasingCurvei(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0,
    qreal destination,
    const QEasingCurve *a2,
    int time) {
  self->move(*a0, destination, *a2, time);
}

//  void QQuickTimeLine::moveBy(QQuickTimeLineValue &a0, qreal change, int
//      time)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine6moveByER19QQuickTimeLineValuedi(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0,
    qreal change,
    int time) {
  self->moveBy(*a0, change, time);
}

//  void QQuickTimeLine::moveBy(QQuickTimeLineValue &a0, qreal change, const
//      QEasingCurve &a2, int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine6moveByER19QQuickTimeLineValuedRK12QEasingCurvei(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0,
    qreal change,
    const QEasingCurve *a2,
    int time) {
  self->moveBy(*a0, change, *a2, time);
}

//  void QQuickTimeLine::setSyncPoint(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine12setSyncPointEi(
    QQuickTimeLine *self,
    int a0) {
  self->setSyncPoint(a0);
}

//  int QQuickTimeLine::syncPoint() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTimeLine9syncPointEv(const QQuickTimeLine *self) {
  return self->syncPoint();
}

//  void QQuickTimeLine::sync(QQuickTimeLineValue &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine4syncER19QQuickTimeLineValue(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0) {
  self->sync(*a0);
}

//  void QQuickTimeLine::sync(QQuickTimeLineValue &a0, QQuickTimeLineValue
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine4syncER19QQuickTimeLineValueS1_(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0,
    QQuickTimeLineValue *a1) {
  self->sync(*a0, *a1);
}

//  void QQuickTimeLine::reset(QQuickTimeLineValue &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine5resetER19QQuickTimeLineValue(
    QQuickTimeLine *self,
    QQuickTimeLineValue *a0) {
  self->reset(*a0);
}

//  void QQuickTimeLine::complete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine8completeEv(QQuickTimeLine *self) {
  self->complete();
}

//  void QQuickTimeLine::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine5clearEv(QQuickTimeLine *self) {
  self->clear();
}

//  bool QQuickTimeLine::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTimeLine8isActiveEv(const QQuickTimeLine *self) {
  return self->isActive();
}

//  int QQuickTimeLine::time() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTimeLine4timeEv(const QQuickTimeLine *self) {
  return self->time();
}

//  int QQuickTimeLine::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTimeLine8durationEv(const QQuickTimeLine *self) {
  return self->duration();
}

//  void QQuickTimeLine::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine7updatedEv(QQuickTimeLine *self) {
  self->updated();
}

//  void QQuickTimeLine::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine17updateCurrentTimeEi(
    QQuickTimeLine *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  void QQuickTimeLine::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QQuickTimeLine14debugAnimationE6QDebug(
    const QQuickTimeLine *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  void QQuickTimeLine::remove(QQuickTimeLineObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTimeLine6removeEP20QQuickTimeLineObject(
    QQuickTimeLine *self,
    QQuickTimeLineObject *a0) {
  self->remove(a0);
}

//  QQuickTimeLine as the QAbstractAnimationJob it is built on
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_cast_QQuickTimeLine_QAbstractAnimationJob(
    QQuickTimeLine *self) {
  return static_cast<QAbstractAnimationJob *>(self);
}

//  a Python function taken by a CuteQQuickTimeLine, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTimeLine(
    QQuickTimeLine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTimeLine *>(self)->take(key, call);
}

//  int QQuickTimeLine::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QQuickTimeLine8durationEv(const QQuickTimeLine *self) {
  return self->QQuickTimeLine::duration();
}

//  void QQuickTimeLine::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTimeLine17updateCurrentTimeEi(
    QQuickTimeLine *self,
    int a0) {
  static_cast<OwnQQuickTimeLine *>(self)->OwnQQuickTimeLine::updateCurrentTime(
      a0);
}

//  void QQuickTimeLine::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK14QQuickTimeLine14debugAnimationE6QDebug(
    const QQuickTimeLine *self,
    const QDebug *d) {
  static_cast<const OwnQQuickTimeLine *>(self)->OwnQQuickTimeLine::debugAnimation(
      *d);
}
