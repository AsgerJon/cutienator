//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QAnimationTimer' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 8 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/qabstractanimation.h>
#include <QtCore/qanimationgroup.h>
#include <QtCore/qdebug.h>
#include <QtCore/private/qabstractanimation_p.h>
#if defined(Q_OS_WASM)
#include <QtCore/private/qwasmanimationdriver_p.h>
#endif
#include <QtCore/qmath.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qpointer.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/q26numeric.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/animation/qabstractanimation.cpp, line 134, as local:qabstractanimation.cpp:AnimationListConstIt
typedef QList<QAbstractAnimation*>::ConstIterator AnimationListConstIt;

//  from QtCore__QAnimationTimer.cpp, line 1, as moc:QAnimationTimer
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15QAnimationTimerE_t {};
} // unnamed namespace

template <> constexpr inline auto QAnimationTimer::qt_create_metaobjectdata<qt_meta_tag_ZN15QAnimationTimerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QAnimationTimer",
        "startAnimations",
        "",
        "stopTimer"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'startAnimations'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'stopTimer'
        QtMocHelpers::SlotData<void()>(3, 2, QMC::AccessPrivate, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QAnimationTimer, qt_meta_tag_ZN15QAnimationTimerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QAnimationTimer::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstractAnimationTimer::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QAnimationTimerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QAnimationTimerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15QAnimationTimerE_t>.metaTypes,
    nullptr
} };

void QAnimationTimer::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QAnimationTimer *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->startAnimations(); break;
        case 1: _t->stopTimer(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *QAnimationTimer::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QAnimationTimer::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QAnimationTimerE_t>.strings))
        return static_cast<void*>(this);
    return QAbstractAnimationTimer::qt_metacast(_clname);
}

int QAnimationTimer::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstractAnimationTimer::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP

//  from src/corelib/animation/qabstractanimation.cpp, line 624, as _ZN15QAnimationTimer15startAnimationsEv
inline void QAnimationTimer::startAnimations()
{
    if (!startAnimationPending)
        return;
    startAnimationPending = false;

    //force timer to update, which prevents large deltas for our newly added animations
    QUnifiedTimer::instance()->maybeUpdateAnimationsToCurrentTime();

    //we transfer the waiting animations into the "really running" state
    animations += animationsToStart;
    animationsToStart.clear();
    if (!animations.isEmpty())
        restartAnimationTimer();
}

//  from src/corelib/animation/qabstractanimation.cpp, line 584, as _ZN15QAnimationTimer20updateAnimationsTimeEx
inline void QAnimationTimer::updateAnimationsTime(qint64 delta)
{
    //setCurrentTime can get this called again while we're the for loop. At least with pauseAnimations
    if (insideTick)
        return;

    lastTick += delta;

    //we make sure we only call update time if the time has actually changed
    //it might happen in some cases that the time doesn't change because events are delayed
    //when the CPU load is high
    if (delta) {
        QScopedValueRollback<bool> guard(insideTick, true);
        for (currentAnimationIdx = 0; currentAnimationIdx < animations.size(); ++currentAnimationIdx) {
            QAbstractAnimation *animation = animations.at(currentAnimationIdx);
            qint64 elapsed = QAbstractAnimationPrivate::get(animation)->totalCurrentTime
                          + (animation->direction() == QAbstractAnimation::Forward ? delta : -delta);
            animation->setCurrentTime(q26::saturating_cast<int>(elapsed));
        }
        currentAnimationIdx = 0;
    }
}

//  from src/corelib/animation/qabstractanimation.cpp, line 614, as _ZN15QAnimationTimer21restartAnimationTimerEv
inline void QAnimationTimer::restartAnimationTimer()
{
    if (runningLeafAnimations == 0 && !runningPauseAnimations.isEmpty())
        QUnifiedTimer::pauseAnimationTimer(this, closestPauseAnimationTimeToFinish());
    else if (isPaused)
        QUnifiedTimer::resumeAnimationTimer(this);
    else if (!isRegistered)
        QUnifiedTimer::startAnimationTimer(this);
}

//  from src/corelib/animation/qabstractanimation.cpp, line 640, as _ZN15QAnimationTimer9stopTimerEv
inline void QAnimationTimer::stopTimer()
{
    stopTimerPending = false;
    bool pendingStart = startAnimationPending && animationsToStart.size() > 0;
    if (animations.isEmpty() && !pendingStart) {
        QUnifiedTimer::resumeAnimationTimer(this);
        QUnifiedTimer::stopAnimationTimer(this);
        // invalidate the start reference time
        lastTick = 0;
    }
}

//  from src/corelib/animation/qabstractanimation.cpp, line 549, as _ZN15QAnimationTimerD0Ev
inline QAnimationTimer::~QAnimationTimer()
    = default;

//  from src/corelib/animation/qabstractanimation.cpp, line 541, as _ZN15QAnimationTimerC1Ev
inline QAnimationTimer::QAnimationTimer() :
    QAbstractAnimationTimer(), lastTick(0),
    currentAnimationIdx(0), insideTick(false),
    startAnimationPending(false), stopTimerPending(false),
    runningLeafAnimations(0)
{
}

//  from src/corelib/animation/qabstractanimation.cpp, line 571, as _ZN15QAnimationTimer8instanceEv
inline QAnimationTimer *QAnimationTimer::instance()
{
    return instance(true);
}

//  from src/corelib/animation/qabstractanimation.cpp, line 552, as _ZN15QAnimationTimer8instanceEb
inline QAnimationTimer *QAnimationTimer::instance(bool create)
{
    QAnimationTimer *inst;
#if QT_CONFIG(thread)
    static thread_local std::unique_ptr<QAnimationTimer> animationTimer;
    if (create && !animationTimer) {
        inst = new QAnimationTimer;
        animationTimer.reset(inst);
    } else {
        inst = animationTimer.get();
    }
#else
    Q_UNUSED(create);
    static QAnimationTimer animationTimer;
    inst = &animationTimer;
#endif
    return inst;
}

//  from src/corelib/animation/qabstractanimation.cpp, line 652, as _ZN15QAnimationTimer17registerAnimationEP18QAbstractAnimationb
inline void QAnimationTimer::registerAnimation(QAbstractAnimation *animation, bool isTopLevel)
{
    QAnimationTimer *inst = instance(true); //we create the instance if needed
    inst->registerRunningAnimation(animation);
    if (isTopLevel) {
        Q_ASSERT(!QAbstractAnimationPrivate::get(animation)->hasRegisteredTimer);
        QAbstractAnimationPrivate::get(animation)->hasRegisteredTimer = true;
        inst->animationsToStart << animation;
        if (!inst->startAnimationPending) {
            inst->startAnimationPending = true;
            QMetaObject::invokeMethod(inst, "startAnimations", Qt::QueuedConnection);
        }
    }
}

//  from src/corelib/animation/qabstractanimation.cpp, line 667, as _ZN15QAnimationTimer19unregisterAnimationEP18QAbstractAnimation
inline void QAnimationTimer::unregisterAnimation(QAbstractAnimation *animation)
{
    QAnimationTimer *inst = QAnimationTimer::instance(false);
    if (inst) {
        //at this point the unified timer should have been created
        //but it might also have been already destroyed in case the application is shutting down

        inst->unregisterRunningAnimation(animation);

        if (!QAbstractAnimationPrivate::get(animation)->hasRegisteredTimer)
            return;

        int idx = inst->animations.indexOf(animation);
        if (idx != -1) {
            inst->animations.removeAt(idx);
            // this is needed if we unregister an animation while its running
            if (idx <= inst->currentAnimationIdx)
                --inst->currentAnimationIdx;

            if (inst->animations.isEmpty() && !inst->stopTimerPending) {
                inst->stopTimerPending = true;
                QMetaObject::invokeMethod(inst, "stopTimer", Qt::QueuedConnection);
            }
        } else {
            inst->animationsToStart.removeOne(animation);
        }
    }
    QAbstractAnimationPrivate::get(animation)->hasRegisteredTimer = false;
}

//  from src/corelib/animation/qabstractanimation.cpp, line 576, as _ZN15QAnimationTimer17ensureTimerUpdateEv
inline void QAnimationTimer::ensureTimerUpdate()
{
    QAnimationTimer *inst = QAnimationTimer::instance(false);
    QUnifiedTimer *instU = QUnifiedTimer::instance(false);
    if (instU && inst && inst->isPaused)
        instU->updateAnimationTimers();
}

//  from src/corelib/animation/qabstractanimation.cpp, line 607, as _ZN15QAnimationTimer20updateAnimationTimerEv
inline void QAnimationTimer::updateAnimationTimer()
{
    QAnimationTimer *inst = QAnimationTimer::instance(false);
    if (inst)
        inst->restartAnimationTimer();
}

//  from src/corelib/animation/qabstractanimation.cpp, line 697, as _ZN15QAnimationTimer24registerRunningAnimationEP18QAbstractAnimation
inline void QAnimationTimer::registerRunningAnimation(QAbstractAnimation *animation)
{
    if (QAbstractAnimationPrivate::get(animation)->isGroup)
        return;

    if (QAbstractAnimationPrivate::get(animation)->isPause) {
        runningPauseAnimations << animation;
    } else
        runningLeafAnimations++;
}

//  from src/corelib/animation/qabstractanimation.cpp, line 708, as _ZN15QAnimationTimer26unregisterRunningAnimationEP18QAbstractAnimation
inline void QAnimationTimer::unregisterRunningAnimation(QAbstractAnimation *animation)
{
    if (QAbstractAnimationPrivate::get(animation)->isGroup)
        return;

    if (QAbstractAnimationPrivate::get(animation)->isPause)
        runningPauseAnimations.removeOne(animation);
    else
        runningLeafAnimations--;
    Q_ASSERT(runningLeafAnimations >= 0);
}

//  from src/corelib/animation/qabstractanimation.cpp, line 720, as _ZN15QAnimationTimer33closestPauseAnimationTimeToFinishEv
inline int QAnimationTimer::closestPauseAnimationTimeToFinish()
{
    int closestTimeToFinish = INT_MAX;
    for (AnimationListConstIt it = runningPauseAnimations.constBegin(), cend = runningPauseAnimations.constEnd(); it != cend; ++it) {
        const QAbstractAnimation *animation = *it;
        int timeToFinish;

        if (animation->direction() == QAbstractAnimation::Forward)
            timeToFinish = animation->duration() - animation->currentLoopTime();
        else
            timeToFinish = animation->currentLoopTime();

        if (timeToFinish < closestTimeToFinish)
            closestTimeToFinish = timeToFinish;
    }
    return closestTimeToFinish;
}
//  -----------------------------------------------------------------------

//  A QAnimationTimer that Python can take functions over in. Every QAnimationTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef void (*CuteQAnimationTimerCall0)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQAnimationTimerCall1)(const void *, qint64, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef qsizetype (*CuteQAnimationTimerCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAnimationTimerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAnimationTimerCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAnimationTimer : public QAnimationTimer {
public:
  using QAnimationTimer::QAnimationTimer;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN23QAbstractAnimationTimer21restartAnimationTimerEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN23QAbstractAnimationTimer20updateAnimationsTimeEx")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK23QAbstractAnimationTimer21runningAnimationCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(animation)
  //  void QAnimationTimer::restartAnimationTimer()
  void restartAnimationTimer() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAnimationTimerCall0 call = reinterpret_cast<CuteQAnimationTimerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationTimer::restartAnimationTimer();
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAnimationTimer::updateAnimationsTime(qint64 delta)
  void updateAnimationsTime(qint64 delta) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAnimationTimerCall1 call = reinterpret_cast<CuteQAnimationTimerCall1>(taken[1]);
      call(this, delta, &handled);
      if (handled) return;
    }
    QAnimationTimer::updateAnimationsTime(delta);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  qsizetype QAnimationTimer::runningAnimationCount() const
  qsizetype runningAnimationCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAnimationTimerCall2 call = reinterpret_cast<CuteQAnimationTimerCall2>(taken[2]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QAnimationTimer::runningAnimationCount();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAnimationTimerCall3 call = reinterpret_cast<CuteQAnimationTimerCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAnimationTimerCall4 call = reinterpret_cast<CuteQAnimationTimerCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAnimationTimerCall5 call = reinterpret_cast<CuteQAnimationTimerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAnimationTimerCall6 call = reinterpret_cast<CuteQAnimationTimerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAnimationTimerCall7 call = reinterpret_cast<CuteQAnimationTimerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAnimationTimerCall8 call = reinterpret_cast<CuteQAnimationTimerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAnimationTimerCall9 call = reinterpret_cast<CuteQAnimationTimerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAnimationTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAnimationTimer10metaObjectEv(
    const QAnimationTimer *self) {
  return self->metaObject();
}

//  void *QAnimationTimer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QAnimationTimer11qt_metacastEPKc(
    QAnimationTimer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAnimationTimer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QAnimationTimer11qt_metacallEN11QMetaObject4CallEiPPv(
    QAnimationTimer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAnimationTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAnimationTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAnimationTimer::tr(s, c, n));
}

//  QAnimationTimer::QAnimationTimer()
extern "C" Q_DECL_EXPORT
QAnimationTimer *ritual_ZN15QAnimationTimerC1Ev() {
  return new CuteQAnimationTimer();
}

//  QAnimationTimer::~QAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimerD1Ev(QAnimationTimer *self) {
  delete self;
}

//  QAnimationTimer *QAnimationTimer::instance()
extern "C" Q_DECL_EXPORT
QAnimationTimer *ritual_ZN15QAnimationTimer8instanceEv() {
  return QAnimationTimer::instance();
}

//  QAnimationTimer *QAnimationTimer::instance(bool create)
extern "C" Q_DECL_EXPORT
QAnimationTimer *ritual_ZN15QAnimationTimer8instanceEb(bool create) {
  return QAnimationTimer::instance(create);
}

//  void QAnimationTimer::registerAnimation(QAbstractAnimation *animation,
//      bool isTopLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer17registerAnimationEP18QAbstractAnimationb(
    QAbstractAnimation *animation,
    bool isTopLevel) {
  QAnimationTimer::registerAnimation(animation, isTopLevel);
}

//  void QAnimationTimer::unregisterAnimation(QAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer19unregisterAnimationEP18QAbstractAnimation(
    QAbstractAnimation *animation) {
  QAnimationTimer::unregisterAnimation(animation);
}

//  void QAnimationTimer::ensureTimerUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer17ensureTimerUpdateEv() {
  QAnimationTimer::ensureTimerUpdate();
}

//  void QAnimationTimer::updateAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer20updateAnimationTimerEv() {
  QAnimationTimer::updateAnimationTimer();
}

//  void QAnimationTimer::restartAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer21restartAnimationTimerEv(
    QAnimationTimer *self) {
  self->restartAnimationTimer();
}

//  void QAnimationTimer::updateAnimationsTime(qint64 delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer20updateAnimationsTimeEx(
    QAnimationTimer *self,
    qint64 delta) {
  self->updateAnimationsTime(delta);
}

//  qsizetype QAnimationTimer::runningAnimationCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QAnimationTimer21runningAnimationCountEv(
    const QAnimationTimer *self) {
  return self->runningAnimationCount();
}

//  void QAnimationTimer::startAnimations()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer15startAnimationsEv(QAnimationTimer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAnimationTimer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "startAnimations()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "startAnimations()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAnimationTimer::stopTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer9stopTimerEv(QAnimationTimer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAnimationTimer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "stopTimer()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "stopTimer()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAnimationTimer::registerRunningAnimation(QAbstractAnimation
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer24registerRunningAnimationEP18QAbstractAnimation(
    QAnimationTimer *self,
    QAbstractAnimation *animation) {
  self->registerRunningAnimation(animation);
}

//  void QAnimationTimer::unregisterRunningAnimation(QAbstractAnimation
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer26unregisterRunningAnimationEP18QAbstractAnimation(
    QAnimationTimer *self,
    QAbstractAnimation *animation) {
  self->unregisterRunningAnimation(animation);
}

//  int QAnimationTimer::closestPauseAnimationTimeToFinish()
extern "C" Q_DECL_EXPORT
int ritual_ZN15QAnimationTimer33closestPauseAnimationTimeToFinishEv(
    QAnimationTimer *self) {
  return self->closestPauseAnimationTimeToFinish();
}

//  a Python function taken by a CuteQAnimationTimer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAnimationTimer(
    QAnimationTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAnimationTimer *>(self)->take(key, call);
}

//  void QAnimationTimer::restartAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAnimationTimer21restartAnimationTimerEv(
    QAnimationTimer *self) {
  self->QAnimationTimer::restartAnimationTimer();
}

//  void QAnimationTimer::updateAnimationsTime(qint64 delta)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAnimationTimer20updateAnimationsTimeEx(
    QAnimationTimer *self,
    qint64 delta) {
  self->QAnimationTimer::updateAnimationsTime(delta);
}

//  qsizetype QAnimationTimer::runningAnimationCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK15QAnimationTimer21runningAnimationCountEv(
    const QAnimationTimer *self) {
  return self->QAnimationTimer::runningAnimationCount();
}

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(animation)
