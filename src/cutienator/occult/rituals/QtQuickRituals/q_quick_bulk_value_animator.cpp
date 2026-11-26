//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qeasingcurve.h>
#include <QtCore/qdebug.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickanimation_p.h>
#include <QtQuick/private/qquickanimation_p_p.h>
#include <QtQuick/private/qquickanimatorjob_p.h>
#include <QtQuick/private/qquickstatechangescript_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/qqmlpropertyvaluesource.h>
#include <QtQml/qqml.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlexpression.h>
#include <QtQml/private/qqmlstringconverters_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlmetatype_p.h>
#include <QtQml/private/qqmlvaluetype_p.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtCore/qfile.h>
#include <QtQml/private/qparallelanimationgroupjob_p.h>
#include <QtQml/private/qsequentialanimationgroupjob_p.h>
#include <QtCore/qset.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 2062, as _ZN23QQuickBulkValueAnimator17updateCurrentTimeEi
inline void QQuickBulkValueAnimator::updateCurrentTime(int currentTime)
{
    if (isStopped())
        return;

    const qreal progress = easing.valueForProgress(((m_duration == 0) ? qreal(1) : qreal(currentTime) / qreal(m_duration)));

    if (animValue)
        animValue->setValue(progress);
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 2073, as _ZN23QQuickBulkValueAnimator28topLevelAnimationLoopChangedEv
inline void QQuickBulkValueAnimator::topLevelAnimationLoopChanged()
{
    // Check for new "from" value only when animation has one loop.
    // Otherwise use the initial "from" value for every iteration.
    if (m_loopCount == 1 && fromIsSourced)
        *fromIsSourced = false;
    QAbstractAnimationJob::topLevelAnimationLoopChanged();
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 2050, as _ZN23QQuickBulkValueAnimatorD2Ev
inline QQuickBulkValueAnimator::~QQuickBulkValueAnimator()
{
    delete animValue;
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 2082, as _ZNK23QQuickBulkValueAnimator14debugAnimationE6QDebug
inline void QQuickBulkValueAnimator::debugAnimation(QDebug d) const
{
    d << "BulkValueAnimation(" << Qt::hex << (const void *) this << Qt::dec << ")" << "duration:" << duration();

    if (animValue) {
        int indentLevel = 1;
        const QAbstractAnimationJob *job = this;
        while ((job = job->group()))
            ++indentLevel;
        animValue->debugUpdater(d, indentLevel);
    }
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 2045, as _ZN23QQuickBulkValueAnimatorC1Ev
inline QQuickBulkValueAnimator::QQuickBulkValueAnimator()
    : QAbstractAnimationJob(), animValue(nullptr), fromIsSourced(nullptr), m_duration(250)
{
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 2055, as _ZN23QQuickBulkValueAnimator12setAnimValueEP22QQuickBulkValueUpdater
inline void QQuickBulkValueAnimator::setAnimValue(QQuickBulkValueUpdater *value)
{
    if (isRunning())
        stop();
    animValue = value;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickBulkValueAnimator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickBulkValueAnimator : QQuickBulkValueAnimator {
  using QQuickBulkValueAnimator::updateCurrentTime;
  using QQuickBulkValueAnimator::topLevelAnimationLoopChanged;
  using QQuickBulkValueAnimator::debugAnimation;
};

//  A QQuickBulkValueAnimator that Python can take functions over in. Every QQuickBulkValueAnimator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQQuickBulkValueAnimatorCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickBulkValueAnimatorCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickBulkValueAnimatorCall2)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickBulkValueAnimatorCall3)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickBulkValueAnimatorCall4)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickBulkValueAnimatorCall5)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickBulkValueAnimatorCall6)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickBulkValueAnimator : public QQuickBulkValueAnimator {
public:
  using QQuickBulkValueAnimator::QQuickBulkValueAnimator;
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
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv")) {
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
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  int QQuickBulkValueAnimator::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickBulkValueAnimatorCall0 call = reinterpret_cast<CuteQQuickBulkValueAnimatorCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickBulkValueAnimator::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickBulkValueAnimator::updateCurrentTime(int currentTime)
  void updateCurrentTime(int currentTime) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickBulkValueAnimatorCall1 call = reinterpret_cast<CuteQQuickBulkValueAnimatorCall1>(taken[1]);
      call(this, currentTime, &handled);
      if (handled) return;
    }
    QQuickBulkValueAnimator::updateCurrentTime(currentTime);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickBulkValueAnimator::topLevelAnimationLoopChanged()
  void topLevelAnimationLoopChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickBulkValueAnimatorCall2 call = reinterpret_cast<CuteQQuickBulkValueAnimatorCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBulkValueAnimator::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickBulkValueAnimator::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickBulkValueAnimatorCall3 call = reinterpret_cast<CuteQQuickBulkValueAnimatorCall3>(taken[3]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QQuickBulkValueAnimator::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickBulkValueAnimatorCall4 call = reinterpret_cast<CuteQQuickBulkValueAnimatorCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQQuickBulkValueAnimatorCall5 call = reinterpret_cast<CuteQQuickBulkValueAnimatorCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuickBulkValueAnimatorCall6 call = reinterpret_cast<CuteQQuickBulkValueAnimatorCall6>(taken[6]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickBulkValueAnimator::QQuickBulkValueAnimator()
extern "C" Q_DECL_EXPORT
QQuickBulkValueAnimator *ritual_ZN23QQuickBulkValueAnimatorC1Ev() {
  return new CuteQQuickBulkValueAnimator();
}

//  QQuickBulkValueAnimator::~QQuickBulkValueAnimator()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickBulkValueAnimatorD1Ev(QQuickBulkValueAnimator *self) {
  delete self;
}

//  void QQuickBulkValueAnimator::setAnimValue(QQuickBulkValueUpdater *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickBulkValueAnimator12setAnimValueEP22QQuickBulkValueUpdater(
    QQuickBulkValueAnimator *self,
    QQuickBulkValueUpdater *value) {
  self->setAnimValue(value);
}

//  QQuickBulkValueUpdater *QQuickBulkValueAnimator::getAnimValue() const
extern "C" Q_DECL_EXPORT
QQuickBulkValueUpdater *ritual_ZNK23QQuickBulkValueAnimator12getAnimValueEv(
    const QQuickBulkValueAnimator *self) {
  return self->getAnimValue();
}

//  void QQuickBulkValueAnimator::setFromIsSourcedValue(bool *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickBulkValueAnimator21setFromIsSourcedValueEPb(
    QQuickBulkValueAnimator *self,
    bool *value) {
  self->setFromIsSourcedValue(value);
}

//  int QQuickBulkValueAnimator::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickBulkValueAnimator8durationEv(
    const QQuickBulkValueAnimator *self) {
  return self->duration();
}

//  void QQuickBulkValueAnimator::setDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickBulkValueAnimator11setDurationEi(
    QQuickBulkValueAnimator *self,
    int msecs) {
  self->setDuration(msecs);
}

//  QEasingCurve QQuickBulkValueAnimator::easingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK23QQuickBulkValueAnimator11easingCurveEv(
    const QQuickBulkValueAnimator *self) {
  return new QEasingCurve(self->easingCurve());
}

//  void QQuickBulkValueAnimator::setEasingCurve(const QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickBulkValueAnimator14setEasingCurveERK12QEasingCurve(
    QQuickBulkValueAnimator *self,
    const QEasingCurve *curve) {
  self->setEasingCurve(*curve);
}

//  void QQuickBulkValueAnimator::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickBulkValueAnimator17updateCurrentTimeEi(
    QQuickBulkValueAnimator *self,
    int currentTime) {
  self->updateCurrentTime(currentTime);
}

//  void QQuickBulkValueAnimator::topLevelAnimationLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickBulkValueAnimator28topLevelAnimationLoopChangedEv(
    QQuickBulkValueAnimator *self) {
  self->topLevelAnimationLoopChanged();
}

//  void QQuickBulkValueAnimator::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QQuickBulkValueAnimator14debugAnimationE6QDebug(
    const QQuickBulkValueAnimator *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  a Python function taken by a CuteQQuickBulkValueAnimator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickBulkValueAnimator(
    QQuickBulkValueAnimator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickBulkValueAnimator *>(self)->take(key, call);
}

//  int QQuickBulkValueAnimator::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QQuickBulkValueAnimator8durationEv(
    const QQuickBulkValueAnimator *self) {
  return self->QQuickBulkValueAnimator::duration();
}

//  void QQuickBulkValueAnimator::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickBulkValueAnimator17updateCurrentTimeEi(
    QQuickBulkValueAnimator *self,
    int currentTime) {
  static_cast<OwnQQuickBulkValueAnimator *>(self)->OwnQQuickBulkValueAnimator::updateCurrentTime(
      currentTime);
}

//  void QQuickBulkValueAnimator::topLevelAnimationLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickBulkValueAnimator28topLevelAnimationLoopChangedEv(
    QQuickBulkValueAnimator *self) {
  static_cast<OwnQQuickBulkValueAnimator *>(self)->OwnQQuickBulkValueAnimator::topLevelAnimationLoopChanged();
}

//  void QQuickBulkValueAnimator::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK23QQuickBulkValueAnimator14debugAnimationE6QDebug(
    const QQuickBulkValueAnimator *self,
    const QDebug *d) {
  static_cast<const OwnQQuickBulkValueAnimator *>(self)->OwnQQuickBulkValueAnimator::debugAnimation(
      *d);
}
