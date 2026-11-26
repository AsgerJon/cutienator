//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktransition_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktransition_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <QtQuick/private/qquickstate_p_p.h>
#include <QtQuick/private/qquickstatechangescript_p.h>
#include <QtQuick/private/qquickanimation_p.h>
#include <QtQuick/private/qquickanimation_p_p.h>
#include <QtQuick/private/qquicktransitionmanager_p_p.h>
#include <QtQuick/private/qquickanimatorjob_p.h>
#include <QtQml/private/qparallelanimationgroupjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 84, as local:qquicktransition.cpp:QQuickTransitionPrivate
class QQuickTransitionPrivate : public QObjectPrivate
{
    Q_DECLARE_PUBLIC(QQuickTransition)
public:
    QQuickTransitionPrivate()
    : fromState(QLatin1String("*")), toState(QLatin1String("*"))
    , runningInstanceCount(0), state(QAbstractAnimationJob::Stopped)
    , reversed(false), reversible(false), enabled(true)
    {
    }

    static QQuickTransitionPrivate *get(QQuickTransition *q) { return q->d_func(); }
    void animationStateChanged(QAbstractAnimationJob::State newState);

    QString fromState;
    QString toState;
    quint32 runningInstanceCount;
    QAbstractAnimationJob::State state;
    bool reversed;
    bool reversible;
    bool enabled;
protected:

    static void append_animation(QQmlListProperty<QQuickAbstractAnimation> *list, QQuickAbstractAnimation *a);
    static qsizetype animation_count(QQmlListProperty<QQuickAbstractAnimation> *list);
    static QQuickAbstractAnimation* animation_at(QQmlListProperty<QQuickAbstractAnimation> *list, qsizetype pos);
    static void clear_animations(QQmlListProperty<QQuickAbstractAnimation> *list);
    static void removeLast_animation(QQmlListProperty<QQuickAbstractAnimation> *list);
    static void replace_animation(
            QQmlListProperty<QQuickAbstractAnimation> *list, qsizetype pos,
            QQuickAbstractAnimation *a);

    QList<QPointer<QQuickAbstractAnimation>> animations;
};

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 119, as local:qquicktransition.cpp:QQuickTransitionPrivate::append_animation
inline void QQuickTransitionPrivate::append_animation(QQmlListProperty<QQuickAbstractAnimation> *list, QQuickAbstractAnimation *a)
{
    QQuickTransition *q = static_cast<QQuickTransition *>(list->object);
    q->d_func()->animations.append(a);
    if (a)
        a->setDisableUserControl();
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 127, as local:qquicktransition.cpp:QQuickTransitionPrivate::animation_count
inline qsizetype QQuickTransitionPrivate::animation_count(QQmlListProperty<QQuickAbstractAnimation> *list)
{
    QQuickTransition *q = static_cast<QQuickTransition *>(list->object);
    return q->d_func()->animations.size();
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 133, as local:qquicktransition.cpp:QQuickTransitionPrivate::animation_at
inline QQuickAbstractAnimation* QQuickTransitionPrivate::animation_at(QQmlListProperty<QQuickAbstractAnimation> *list, qsizetype pos)
{
    QQuickTransition *q = static_cast<QQuickTransition *>(list->object);
    return q->d_func()->animations.at(pos);
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 139, as local:qquicktransition.cpp:QQuickTransitionPrivate::clear_animations
inline void QQuickTransitionPrivate::clear_animations(QQmlListProperty<QQuickAbstractAnimation> *list)
{
    QQuickTransition *q = static_cast<QQuickTransition *>(list->object);
    q->d_func()->animations.clear();
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 145, as local:qquicktransition.cpp:QQuickTransitionPrivate::removeLast_animation
inline void QQuickTransitionPrivate::removeLast_animation(QQmlListProperty<QQuickAbstractAnimation> *list)
{
    QQuickTransition *q = static_cast<QQuickTransition *>(list->object);
    q->d_func()->animations.removeLast();
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 151, as local:qquicktransition.cpp:QQuickTransitionPrivate::replace_animation
inline void QQuickTransitionPrivate::replace_animation(
        QQmlListProperty<QQuickAbstractAnimation> *list, qsizetype pos, QQuickAbstractAnimation *a)
{
    QQuickTransition *q = static_cast<QQuickTransition *>(list->object);
    QQuickTransitionPrivate *d = q->d_func();
    if (d->animations.length() <= pos)
        d->animations.resize(pos + 1, nullptr);
    d->animations[pos] = a;
    if (a)
        a->setDisableUserControl();
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 172, as local:qquicktransition.cpp:QQuickTransitionPrivate::animationStateChanged
inline void QQuickTransitionPrivate::animationStateChanged(QAbstractAnimationJob::State newState)
{
    Q_Q(QQuickTransition);

    if (newState == QAbstractAnimationJob::Running) {
        runningInstanceCount++;
        if (runningInstanceCount == 1)
            emit q->runningChanged();
    } else if (newState == QAbstractAnimationJob::Stopped) {
        runningInstanceCount--;
        if (runningInstanceCount == 0)
            emit q->runningChanged();
    }
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 205, as _ZN24QQuickTransitionInstanceD1Ev
inline QQuickTransitionInstance::~QQuickTransitionInstance()
{
    removeStateChangeListener();
    delete m_anim;
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 211, as _ZN24QQuickTransitionInstance5startEv
inline void QQuickTransitionInstance::start()
{
    if (m_anim)
        m_anim->start();
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 217, as _ZN24QQuickTransitionInstance4stopEv
inline void QQuickTransitionInstance::stop()
{
    if (m_anim)
        m_anim->stop();
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 223, as _ZN24QQuickTransitionInstance8completeEv
inline void QQuickTransitionInstance::complete()
{
    if (m_anim)
        m_anim->complete();
}

//  from ../qtdeclarative/src/quick/util/qquicktransition.cpp, line 229, as _ZNK24QQuickTransitionInstance9isRunningEv
inline bool QQuickTransitionInstance::isRunning() const
{
    return m_anim && m_anim->state() == QAbstractAnimationJob::Running;
}
//  -----------------------------------------------------------------------

//  A QQuickTransitionInstance that Python can take functions over in. Every QQuickTransitionInstance
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransitionInstanceCall0)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransitionInstanceCall1)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransitionInstanceCall2)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransitionInstanceCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickTransitionInstance : public QQuickTransitionInstance {
public:
  using QQuickTransitionInstance::QQuickTransitionInstance;
  CuteQQuickTransitionInstance(const QQuickTransitionInstance & other) : QQuickTransitionInstance(other) {}
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstractAnimationJob")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP21QAbstractAnimationJobi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  void
  //      QQuickTransitionInstance::animationStateChanged(QAbstractAnimatio
  //      nJob *a0, QAbstractAnimationJob::State a1,
  //      QAbstractAnimationJob::State a2)
  void animationStateChanged(
      QAbstractAnimationJob *a0,
      QAbstractAnimationJob::State a1,
      QAbstractAnimationJob::State a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTransitionInstanceCall0 call = reinterpret_cast<CuteQQuickTransitionInstanceCall0>(taken[0]);
      call(this, a0, static_cast<int>(a1), static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QQuickTransitionInstance::animationStateChanged(a0, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void
  //      QAnimationJobChangeListener::animationFinished(QAbstractAnimation
  //      Job *a0)
  void animationFinished(QAbstractAnimationJob *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTransitionInstanceCall1 call = reinterpret_cast<CuteQQuickTransitionInstanceCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationFinished(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentLoopChanged(QAbstra
  //      ctAnimationJob *a0)
  void animationCurrentLoopChanged(QAbstractAnimationJob *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTransitionInstanceCall2 call = reinterpret_cast<CuteQQuickTransitionInstanceCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentLoopChanged(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentTimeChanged(QAbstra
  //      ctAnimationJob *a0, int a1)
  void animationCurrentTimeChanged(
      QAbstractAnimationJob *a0,
      int a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTransitionInstanceCall3 call = reinterpret_cast<CuteQQuickTransitionInstanceCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickTransitionInstance::~QQuickTransitionInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTransitionInstanceD1Ev(
    QQuickTransitionInstance *self) {
  delete self;
}

//  void QQuickTransitionInstance::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTransitionInstance5startEv(
    QQuickTransitionInstance *self) {
  self->start();
}

//  void QQuickTransitionInstance::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTransitionInstance4stopEv(
    QQuickTransitionInstance *self) {
  self->stop();
}

//  void QQuickTransitionInstance::complete()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTransitionInstance8completeEv(
    QQuickTransitionInstance *self) {
  self->complete();
}

//  bool QQuickTransitionInstance::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickTransitionInstance9isRunningEv(
    const QQuickTransitionInstance *self) {
  return self->isRunning();
}

//  void
//      QQuickTransitionInstance::animationStateChanged(QAbstractAnimationJob
//      *a0, QAbstractAnimationJob::State a1, QAbstractAnimationJob::State
//      a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTransitionInstance21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_(
    QQuickTransitionInstance *self,
    QAbstractAnimationJob *a0,
    QAbstractAnimationJob::State a1,
    QAbstractAnimationJob::State a2) {
  self->animationStateChanged(a0, a1, a2);
}

//  void QQuickTransitionInstance::removeStateChangeListener()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTransitionInstance25removeStateChangeListenerEv(
    QQuickTransitionInstance *self) {
  self->removeStateChangeListener();
}

//  a Python function taken by a CuteQQuickTransitionInstance, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTransitionInstance(
    QQuickTransitionInstance *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTransitionInstance *>(self)->take(key, call);
}
