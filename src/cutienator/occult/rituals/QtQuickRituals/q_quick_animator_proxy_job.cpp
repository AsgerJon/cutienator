//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickAnimatorProxyJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAnimatorProxyJob : QQuickAnimatorProxyJob {
  using QQuickAnimatorProxyJob::updateCurrentTime;
  using QQuickAnimatorProxyJob::updateLoopCount;
  using QQuickAnimatorProxyJob::updateState;
  using QQuickAnimatorProxyJob::debugAnimation;
};

//  A QQuickAnimatorProxyJob that Python can take functions over in. Every QQuickAnimatorProxyJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQQuickAnimatorProxyJobCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorProxyJobCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorProxyJobCall2)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorProxyJobCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorProxyJobCall4)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorProxyJobCall5)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorProxyJobCall6)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatorProxyJobCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatorProxyJobCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorProxyJobCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorProxyJobCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorProxyJobCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorProxyJobCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorProxyJobCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAnimatorProxyJob : public QQuickAnimatorProxyJob {
public:
  using QQuickAnimatorProxyJob::QQuickAnimatorProxyJob;
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
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateLoopCountEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
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
  //  int QQuickAnimatorProxyJob::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimatorProxyJobCall0 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAnimatorProxyJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickAnimatorProxyJob::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimatorProxyJobCall1 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickAnimatorProxyJob::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickAnimatorProxyJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnimatorProxyJobCall2 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickAnimatorProxyJob::updateLoopCount(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickAnimatorProxyJob::updateState(QAbstractAnimationJob::State
  //      newState, QAbstractAnimationJob::State oldState)
  void updateState(
      QAbstractAnimationJob::State newState,
      QAbstractAnimationJob::State oldState) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnimatorProxyJobCall3 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall3>(taken[3]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QQuickAnimatorProxyJob::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickAnimatorProxyJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAnimatorProxyJobCall4 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall4>(taken[4]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QQuickAnimatorProxyJob::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateDirection(QAbstractAnimationJob::Di
  //      rection direction)
  void updateDirection(QAbstractAnimationJob::Direction direction) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAnimatorProxyJobCall5 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall5>(taken[5]);
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
      CuteQQuickAnimatorProxyJobCall6 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall6>(taken[6]);
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
      CuteQQuickAnimatorProxyJobCall7 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall7>(taken[7]);
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
      CuteQQuickAnimatorProxyJobCall8 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall8>(taken[8]);
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
      CuteQQuickAnimatorProxyJobCall9 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall9>(taken[9]);
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
      CuteQQuickAnimatorProxyJobCall10 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall10>(taken[10]);
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
      CuteQQuickAnimatorProxyJobCall11 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall11>(taken[11]);
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
      CuteQQuickAnimatorProxyJobCall12 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall12>(taken[12]);
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
      CuteQQuickAnimatorProxyJobCall13 call = reinterpret_cast<CuteQQuickAnimatorProxyJobCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAnimatorProxyJob::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickAnimatorProxyJob10metaObjectEv(
    const QQuickAnimatorProxyJob *self) {
  return self->metaObject();
}

//  QString QQuickAnimatorProxyJob::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickAnimatorProxyJob2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAnimatorProxyJob::tr(s, c, n));
}

//  QQuickAnimatorProxyJob::QQuickAnimatorProxyJob(QAbstractAnimationJob
//      *job, QQuickAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
QQuickAnimatorProxyJob *ritual_ZN22QQuickAnimatorProxyJobC1EP21QAbstractAnimationJobP23QQuickAbstractAnimation(
    QAbstractAnimationJob *job,
    QQuickAbstractAnimation *animation) {
  return new CuteQQuickAnimatorProxyJob(job, animation);
}

//  QQuickAnimatorProxyJob::~QQuickAnimatorProxyJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickAnimatorProxyJobD1Ev(QQuickAnimatorProxyJob *self) {
  delete self;
}

//  int QQuickAnimatorProxyJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickAnimatorProxyJob8durationEv(
    const QQuickAnimatorProxyJob *self) {
  return self->duration();
}

//  void QQuickAnimatorProxyJob::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickAnimatorProxyJob17updateCurrentTimeEi(
    QQuickAnimatorProxyJob *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  void QQuickAnimatorProxyJob::updateLoopCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickAnimatorProxyJob15updateLoopCountEi(
    QQuickAnimatorProxyJob *self,
    int a0) {
  self->updateLoopCount(a0);
}

//  void QQuickAnimatorProxyJob::updateState(QAbstractAnimationJob::State
//      newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickAnimatorProxyJob11updateStateEN21QAbstractAnimationJob5StateES1_(
    QQuickAnimatorProxyJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  self->updateState(newState, oldState);
}

//  void QQuickAnimatorProxyJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QQuickAnimatorProxyJob14debugAnimationE6QDebug(
    const QQuickAnimatorProxyJob *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  void QQuickAnimatorProxyJob::windowChanged(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickAnimatorProxyJob13windowChangedEP12QQuickWindow(
    QQuickAnimatorProxyJob *self,
    QQuickWindow *window) {
  self->windowChanged(window);
}

//  void QQuickAnimatorProxyJob::sceneGraphInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickAnimatorProxyJob21sceneGraphInitializedEv(
    QQuickAnimatorProxyJob *self) {
  self->sceneGraphInitialized();
}

//  void QQuickAnimatorProxyJob::syncBackCurrentValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickAnimatorProxyJob21syncBackCurrentValuesEv(
    QQuickAnimatorProxyJob *self) {
  self->syncBackCurrentValues();
}

//  void QQuickAnimatorProxyJob::readyToAnimate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickAnimatorProxyJob14readyToAnimateEv(
    QQuickAnimatorProxyJob *self) {
  self->readyToAnimate();
}

//  void QQuickAnimatorProxyJob::setWindow(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickAnimatorProxyJob9setWindowEP12QQuickWindow(
    QQuickAnimatorProxyJob *self,
    QQuickWindow *window) {
  self->setWindow(window);
}

//  QObject
//      *QQuickAnimatorProxyJob::findAnimationContext(QQuickAbstractAnimation
//      *a0)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN22QQuickAnimatorProxyJob20findAnimationContextEP23QQuickAbstractAnimation(
    QQuickAbstractAnimation *a0) {
  return QQuickAnimatorProxyJob::findAnimationContext(a0);
}

//  QQuickAnimatorProxyJob as the QAbstractAnimationJob it is built on
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_cast_QQuickAnimatorProxyJob_QAbstractAnimationJob(
    QQuickAnimatorProxyJob *self) {
  return static_cast<QAbstractAnimationJob *>(self);
}

//  a Python function taken by a CuteQQuickAnimatorProxyJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimatorProxyJob(
    QQuickAnimatorProxyJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimatorProxyJob *>(self)->take(key, call);
}

//  int QQuickAnimatorProxyJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QQuickAnimatorProxyJob8durationEv(
    const QQuickAnimatorProxyJob *self) {
  return self->QQuickAnimatorProxyJob::duration();
}

//  void QQuickAnimatorProxyJob::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickAnimatorProxyJob17updateCurrentTimeEi(
    QQuickAnimatorProxyJob *self,
    int a0) {
  static_cast<OwnQQuickAnimatorProxyJob *>(self)->OwnQQuickAnimatorProxyJob::updateCurrentTime(
      a0);
}

//  void QQuickAnimatorProxyJob::updateLoopCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickAnimatorProxyJob15updateLoopCountEi(
    QQuickAnimatorProxyJob *self,
    int a0) {
  static_cast<OwnQQuickAnimatorProxyJob *>(self)->OwnQQuickAnimatorProxyJob::updateLoopCount(
      a0);
}

//  void QQuickAnimatorProxyJob::updateState(QAbstractAnimationJob::State
//      newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickAnimatorProxyJob11updateStateEN21QAbstractAnimationJob5StateES1_(
    QQuickAnimatorProxyJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  static_cast<OwnQQuickAnimatorProxyJob *>(self)->OwnQQuickAnimatorProxyJob::updateState(
      newState,
      oldState);
}

//  void QQuickAnimatorProxyJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK22QQuickAnimatorProxyJob14debugAnimationE6QDebug(
    const QQuickAnimatorProxyJob *self,
    const QDebug *d) {
  static_cast<const OwnQQuickAnimatorProxyJob *>(self)->OwnQQuickAnimatorProxyJob::debugAnimation(
      *d);
}
