//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qclock_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qclock_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/qclock.h>
#include <Qt3DAnimation/private/qclock_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/frontend/qclock.cpp, line 11, as _ZN13Qt3DAnimation13QClockPrivateC1Ev
namespace Qt3DAnimation {
inline QClockPrivate::QClockPrivate()
    : Qt3DCore::QNodePrivate()
    , m_playbackRate(1.0f)
{
}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  A Qt3DAnimation::QClockPrivate that Python can take functions over in. Every Qt3DAnimation::QClockPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_QClockPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DAnimation_QClockPrivateCall1)(const void *, int *);
class CuteQt3DAnimation_QClockPrivate : public Qt3DAnimation::QClockPrivate {
public:
  using Qt3DAnimation::QClockPrivate::QClockPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_QClockPrivateCall0 call = reinterpret_cast<CuteQt3DAnimation_QClockPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QClockPrivateCall1 call = reinterpret_cast<CuteQt3DAnimation_QClockPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DAnimation::QClockPrivate::QClockPrivate()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClockPrivate *ritual_ZN13Qt3DAnimation13QClockPrivateC1Ev() {
  return new CuteQt3DAnimation_QClockPrivate();
}

//  QClock *Qt3DAnimation::QClockPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClock *ritual_ZN13Qt3DAnimation13QClockPrivate6q_funcEv(
    Qt3DAnimation::QClockPrivate *self) {
  return self->q_func();
}

//  const QClock *Qt3DAnimation::QClockPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QClock *ritual_ZNK13Qt3DAnimation13QClockPrivate6q_funcEv(
    const Qt3DAnimation::QClockPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DAnimation_QClockPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QClockPrivate(
    Qt3DAnimation::QClockPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QClockPrivate *>(self)->take(key, call);
}
