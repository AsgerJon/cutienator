//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qaxisaccumulator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qaxisaccumulator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/qaxisaccumulator.h>
#include <Qt3DInput/private/qaxisaccumulator_p.h>
#include <Qt3DInput/qaxis.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/frontend/qaxisaccumulator.cpp, line 68, as _ZN9Qt3DInput23QAxisAccumulatorPrivateC1Ev
namespace Qt3DInput {
inline QAxisAccumulatorPrivate::QAxisAccumulatorPrivate()
    : Qt3DCore::QComponentPrivate()
    , m_sourceAxis(nullptr)
    , m_sourceAxisType(QAxisAccumulator::Velocity)
    , m_scale(1.0f)
    , m_value(0.0f)
    , m_velocity(0.0f)
{
}
}  // namespace Qt3DInput

//  from ../qt3d/src/input/frontend/qaxisaccumulator.cpp, line 79, as _ZN9Qt3DInput23QAxisAccumulatorPrivate8setValueEf
namespace Qt3DInput {
inline void QAxisAccumulatorPrivate::setValue(float value)
{
    if (value != m_value) {
        Q_Q(QAxisAccumulator);
        m_value = value;
        const bool wasBlocked = q->blockNotifications(true);
        emit q->valueChanged(m_value);
        q->blockNotifications(wasBlocked);
    }
}
}  // namespace Qt3DInput

//  from ../qt3d/src/input/frontend/qaxisaccumulator.cpp, line 91, as _ZN9Qt3DInput23QAxisAccumulatorPrivate11setVelocityEf
namespace Qt3DInput {
inline void QAxisAccumulatorPrivate::setVelocity(float velocity)
{
    if (velocity != m_velocity) {
        Q_Q(QAxisAccumulator);
        m_velocity = velocity;
        const bool wasBlocked = q->blockNotifications(true);
        emit q->velocityChanged(m_velocity);
        q->blockNotifications(wasBlocked);
    }
}
}  // namespace Qt3DInput
//  -----------------------------------------------------------------------

//  A Qt3DInput::QAxisAccumulatorPrivate that Python can take functions over in. Every Qt3DInput::QAxisAccumulatorPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QAxisAccumulatorPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QAxisAccumulatorPrivateCall1)(const void *, int *);
class CuteQt3DInput_QAxisAccumulatorPrivate : public Qt3DInput::QAxisAccumulatorPrivate {
public:
  using Qt3DInput::QAxisAccumulatorPrivate::QAxisAccumulatorPrivate;
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
      CuteQt3DInput_QAxisAccumulatorPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QAxisAccumulatorPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QAxisAccumulatorPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QAxisAccumulatorPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QAxisAccumulatorPrivate::QAxisAccumulatorPrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisAccumulatorPrivate *ritual_ZN9Qt3DInput23QAxisAccumulatorPrivateC1Ev() {
  return new CuteQt3DInput_QAxisAccumulatorPrivate();
}

//  QAxisAccumulator *Qt3DInput::QAxisAccumulatorPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisAccumulator *ritual_ZN9Qt3DInput23QAxisAccumulatorPrivate6q_funcEv(
    Qt3DInput::QAxisAccumulatorPrivate *self) {
  return self->q_func();
}

//  const QAxisAccumulator *Qt3DInput::QAxisAccumulatorPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAxisAccumulator *ritual_ZNK9Qt3DInput23QAxisAccumulatorPrivate6q_funcEv(
    const Qt3DInput::QAxisAccumulatorPrivate *self) {
  return self->q_func();
}

//  void Qt3DInput::QAxisAccumulatorPrivate::setValue(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QAxisAccumulatorPrivate8setValueEf(
    Qt3DInput::QAxisAccumulatorPrivate *self,
    float value) {
  self->setValue(value);
}

//  void Qt3DInput::QAxisAccumulatorPrivate::setVelocity(float velocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QAxisAccumulatorPrivate11setVelocityEf(
    Qt3DInput::QAxisAccumulatorPrivate *self,
    float velocity) {
  self->setVelocity(velocity);
}

//  a Python function taken by a CuteQt3DInput_QAxisAccumulatorPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAxisAccumulatorPrivate(
    Qt3DInput::QAxisAccumulatorPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAxisAccumulatorPrivate *>(self)->take(key, call);
}
