//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickanimation_p.h"
#include "qquickanimation_p_p.h"
#include "qquickanimatorjob_p.h"
#include <private/qquickstatechangescript_p.h>
#include <private/qqmlcontext_p.h>
#include <qqmlpropertyvaluesource.h>
#include <qqml.h>
#include <qqmlinfo.h>
#include <qqmlexpression.h>
#include <private/qqmlstringconverters_p.h>
#include <private/qqmlglobal_p.h>
#include <private/qqmlmetatype_p.h>
#include <private/qqmlvaluetype_p.h>
#include <private/qqmlproperty_p.h>
#include <private/qqmlengine_p.h>
#include <qvariant.h>
#include <qcolor.h>
#include <qfile.h>
#include "private/qparallelanimationgroupjob_p.h"
#include "private/qsequentialanimationgroupjob_p.h"
#include <QtCore/qset.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 848, as _ZN16QActionAnimationC1Ev
inline QActionAnimation::QActionAnimation()
    : QAbstractAnimationJob(), animAction(nullptr)
{
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 853, as _ZN16QActionAnimationC1EP24QAbstractAnimationAction
inline QActionAnimation::QActionAnimation(QAbstractAnimationAction *action)
    : QAbstractAnimationJob(), animAction(action)
{
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 858, as _ZN16QActionAnimationD1Ev
inline QActionAnimation::~QActionAnimation()
{
    delete animAction;
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 863, as _ZNK16QActionAnimation8durationEv
inline int QActionAnimation::duration() const
{
    return 0;
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 868, as _ZN16QActionAnimation13setAnimActionEP24QAbstractAnimationAction
inline void QActionAnimation::setAnimAction(QAbstractAnimationAction *action)
{
    if (isRunning())
        stop();
    animAction = action;
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 875, as _ZN16QActionAnimation17updateCurrentTimeEi
inline void QActionAnimation::updateCurrentTime(int)
{
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 879, as _ZN16QActionAnimation11updateStateEN21QAbstractAnimationJob5StateES1_
inline void QActionAnimation::updateState(State newState, State oldState)
{
    Q_UNUSED(oldState);

    if (newState == Running) {
        if (animAction) {
            animAction->doAction();
        }
    }
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 890, as _ZNK16QActionAnimation14debugAnimationE6QDebug
inline void QActionAnimation::debugAnimation(QDebug d) const
{
    d << "ActionAnimation(" << Qt::hex << (const void *) this << Qt::dec << ")";

    if (animAction) {
        int indentLevel = 1;
        const QAbstractAnimationJob *job = this;
        while ((job = job->group()))
            ++indentLevel;
        animAction->debugAction(d, indentLevel);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QActionAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQActionAnimation : QActionAnimation {
  using QActionAnimation::updateCurrentTime;
  using QActionAnimation::updateState;
  using QActionAnimation::debugAnimation;
};

//  A QActionAnimation that Python can take functions over in. Every QActionAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQActionAnimationCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQActionAnimationCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQActionAnimationCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQActionAnimationCall3)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQActionAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQActionAnimationCall5)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQActionAnimationCall6)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQActionAnimation : public QActionAnimation {
public:
  using QActionAnimation::QActionAnimation;
  void *taken[7] = {};

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
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateLoopCountEi")) {
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
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  int QActionAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQActionAnimationCall0 call = reinterpret_cast<CuteQActionAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QActionAnimation::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QActionAnimation::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQActionAnimationCall1 call = reinterpret_cast<CuteQActionAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QActionAnimation::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QActionAnimation::updateState(State newState, State oldState)
  void updateState(
      QAbstractAnimationJob::State newState,
      QAbstractAnimationJob::State oldState) override {
    if (taken[2]) {
      int handled = 0;
      CuteQActionAnimationCall2 call = reinterpret_cast<CuteQActionAnimationCall2>(taken[2]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QActionAnimation::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QActionAnimation::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQActionAnimationCall3 call = reinterpret_cast<CuteQActionAnimationCall3>(taken[3]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QActionAnimation::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQActionAnimationCall4 call = reinterpret_cast<CuteQActionAnimationCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateLoopCount(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateDirection(QAbstractAnimationJob::Di
  //      rection direction)
  void updateDirection(QAbstractAnimationJob::Direction direction) override {
    if (taken[5]) {
      int handled = 0;
      CuteQActionAnimationCall5 call = reinterpret_cast<CuteQActionAnimationCall5>(taken[5]);
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
      CuteQActionAnimationCall6 call = reinterpret_cast<CuteQActionAnimationCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QActionAnimation::QActionAnimation()
extern "C" Q_DECL_EXPORT
QActionAnimation *ritual_ZN16QActionAnimationC1Ev() {
  return new CuteQActionAnimation();
}

//  QActionAnimation::QActionAnimation(QAbstractAnimationAction *action)
extern "C" Q_DECL_EXPORT
QActionAnimation *ritual_ZN16QActionAnimationC1EP24QAbstractAnimationAction(
    QAbstractAnimationAction *action) {
  return new CuteQActionAnimation(action);
}

//  QActionAnimation::~QActionAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QActionAnimationD1Ev(QActionAnimation *self) {
  delete self;
}

//  int QActionAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QActionAnimation8durationEv(const QActionAnimation *self) {
  return self->duration();
}

//  void QActionAnimation::setAnimAction(QAbstractAnimationAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QActionAnimation13setAnimActionEP24QAbstractAnimationAction(
    QActionAnimation *self,
    QAbstractAnimationAction *action) {
  self->setAnimAction(action);
}

//  void QActionAnimation::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QActionAnimation17updateCurrentTimeEi(
    QActionAnimation *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  void QActionAnimation::updateState(State newState, State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QActionAnimation11updateStateEN21QAbstractAnimationJob5StateES1_(
    QActionAnimation *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  self->updateState(newState, oldState);
}

//  void QActionAnimation::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QActionAnimation14debugAnimationE6QDebug(
    const QActionAnimation *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  a Python function taken by a CuteQActionAnimation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QActionAnimation(
    QActionAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQActionAnimation *>(self)->take(key, call);
}

//  int QActionAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QActionAnimation8durationEv(
    const QActionAnimation *self) {
  return self->QActionAnimation::duration();
}

//  void QActionAnimation::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QActionAnimation17updateCurrentTimeEi(
    QActionAnimation *self,
    int a0) {
  static_cast<OwnQActionAnimation *>(self)->OwnQActionAnimation::updateCurrentTime(
      a0);
}

//  void QActionAnimation::updateState(State newState, State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QActionAnimation11updateStateEN21QAbstractAnimationJob5StateES1_(
    QActionAnimation *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  static_cast<OwnQActionAnimation *>(self)->OwnQActionAnimation::updateState(
      newState,
      oldState);
}

//  void QActionAnimation::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK16QActionAnimation14debugAnimationE6QDebug(
    const QActionAnimation *self,
    const QDebug *d) {
  static_cast<const OwnQActionAnimation *>(self)->OwnQActionAnimation::debugAnimation(
      *d);
}
