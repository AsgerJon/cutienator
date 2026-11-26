//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickanimatorcontroller_p.h>
#include <QtQuick/private/qquickanimatorjob_p.h>
#include <QtQuick/private/qquickanimator_p.h>
#include <QtQuick/private/qquickanimator_p_p.h>
#include <QtQuick/private/qquickitem_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/private/qquickshadereffect_p.h>
#endif
#include <QtQml/private/qanimationgroupjob_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickanimatorjob.cpp, line 341, as _ZN26QQuickTransformAnimatorJob10invalidateEv
inline void QQuickTransformAnimatorJob::invalidate()
{
    if (m_helper)
        m_helper->node = nullptr;
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorjob.cpp, line 409, as _ZN26QQuickTransformAnimatorJob6commitEv
inline void QQuickTransformAnimatorJob::commit()
{
    if (m_helper)
        m_helper->commit();
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorjob.cpp, line 300, as _ZN26QQuickTransformAnimatorJob9setTargetEP10QQuickItem
inline void QQuickTransformAnimatorJob::setTarget(QQuickItem *item)
{
    // In the extremely unlikely event that the target of an animator has been
    // changed into a new item that sits in the exact same pointer address, we
    // want to force syncing it again.
    if (m_helper && m_target)
        m_helper->wasSynced = false;
    QQuickAnimatorJob::setTarget(item);
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorjob.cpp, line 393, as _ZN26QQuickTransformAnimatorJob6Helper6commitEv
inline void QQuickTransformAnimatorJob::Helper::commit()
{
    if (!wasChanged || !node)
        return;

    QMatrix4x4 m;
    m.translate(dx, dy);
    m.translate(ox, oy);
    m.scale(scale);
    m.rotate(rotation, 0, 0, 1);
    m.translate(-ox, -oy);
    node->setMatrix(m);

    wasChanged = false;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickTransformAnimatorJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTransformAnimatorJob : QQuickTransformAnimatorJob {
  using QQuickTransformAnimatorJob::invalidate;
};

//  A QQuickTransformAnimatorJob that Python can take functions over in. Every QQuickTransformAnimatorJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTransformAnimatorJobCall0)(const void *, int *);
typedef void (*CuteQQuickTransformAnimatorJobCall1)(const void *, int *);
typedef void (*CuteQQuickTransformAnimatorJobCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickTransformAnimatorJobCall3)(const void *, int *);
#if QT_CONFIG(qml_animation)
typedef int (*CuteQQuickTransformAnimatorJobCall4)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransformAnimatorJobCall5)(const void *, QQuickAnimatorController *, int *);
typedef void (*CuteQQuickTransformAnimatorJobCall6)(const void *, int *);
typedef void (*CuteQQuickTransformAnimatorJobCall7)(const void *, int *);
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransformAnimatorJobCall8)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransformAnimatorJobCall9)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransformAnimatorJobCall10)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransformAnimatorJobCall11)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransformAnimatorJobCall12)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickTransformAnimatorJobCall13)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickTransformAnimatorJob : public QQuickTransformAnimatorJob {
public:
  using QQuickTransformAnimatorJob::QQuickTransformAnimatorJob;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob6commitEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob7preSyncEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob9setTargetEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob10invalidateEv")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob8durationEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob10initializeEP24QQuickAnimatorController")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob9writeBackEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob8postSyncEv")) {
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

  //  void QQuickTransformAnimatorJob::commit()
  void commit() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTransformAnimatorJobCall0 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTransformAnimatorJob::commit();
  }

  //  void QQuickTransformAnimatorJob::preSync()
  void preSync() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTransformAnimatorJobCall1 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTransformAnimatorJob::preSync();
  }

  //  void QQuickTransformAnimatorJob::setTarget(QQuickItem *item)
  void setTarget(QQuickItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTransformAnimatorJobCall2 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickTransformAnimatorJob::setTarget(item);
  }

  //  void QQuickTransformAnimatorJob::invalidate()
  void invalidate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTransformAnimatorJobCall3 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTransformAnimatorJob::invalidate();
  }

#if QT_CONFIG(qml_animation)
  //  int QQuickAnimatorJob::duration() const
  int duration() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTransformAnimatorJobCall4 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAnimatorJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

  //  void QQuickAnimatorJob::initialize(QQuickAnimatorController
  //      *controller)
  void initialize(QQuickAnimatorController *controller) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTransformAnimatorJobCall5 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall5>(taken[5]);
      call(this, controller, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::initialize(controller);
  }

  //  void QQuickAnimatorJob::writeBack()
  void writeBack() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTransformAnimatorJobCall6 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAnimatorJob::postSync()
  void postSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTransformAnimatorJobCall7 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::postSync();
  }

#if QT_CONFIG(qml_animation)
  //  void QQuickAnimatorJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTransformAnimatorJobCall8 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall8>(taken[8]);
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
      CuteQQuickTransformAnimatorJobCall9 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall9>(taken[9]);
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
      CuteQQuickTransformAnimatorJobCall10 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall10>(taken[10]);
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
      CuteQQuickTransformAnimatorJobCall11 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall11>(taken[11]);
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
      CuteQQuickTransformAnimatorJobCall12 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall12>(taken[12]);
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
      CuteQQuickTransformAnimatorJobCall13 call = reinterpret_cast<CuteQQuickTransformAnimatorJobCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)
};

//  void QQuickTransformAnimatorJob::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickTransformAnimatorJob6commitEv(
    QQuickTransformAnimatorJob *self) {
  self->commit();
}

//  void QQuickTransformAnimatorJob::preSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickTransformAnimatorJob7preSyncEv(
    QQuickTransformAnimatorJob *self) {
  self->preSync();
}

//  void QQuickTransformAnimatorJob::setTarget(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickTransformAnimatorJob9setTargetEP10QQuickItem(
    QQuickTransformAnimatorJob *self,
    QQuickItem *item) {
  self->setTarget(item);
}

//  void QQuickTransformAnimatorJob::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickTransformAnimatorJob10invalidateEv(
    QQuickTransformAnimatorJob *self) {
  self->invalidate();
}

//  a Python function taken by a CuteQQuickTransformAnimatorJob, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTransformAnimatorJob(
    QQuickTransformAnimatorJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTransformAnimatorJob *>(self)->take(key, call);
}

//  void QQuickTransformAnimatorJob::commit()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickTransformAnimatorJob6commitEv(
    QQuickTransformAnimatorJob *self) {
  self->QQuickTransformAnimatorJob::commit();
}

//  void QQuickTransformAnimatorJob::setTarget(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickTransformAnimatorJob9setTargetEP10QQuickItem(
    QQuickTransformAnimatorJob *self,
    QQuickItem *item) {
  self->QQuickTransformAnimatorJob::setTarget(item);
}

//  void QQuickTransformAnimatorJob::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickTransformAnimatorJob10invalidateEv(
    QQuickTransformAnimatorJob *self) {
  static_cast<OwnQQuickTransformAnimatorJob *>(self)->OwnQQuickTransformAnimatorJob::invalidate();
}
