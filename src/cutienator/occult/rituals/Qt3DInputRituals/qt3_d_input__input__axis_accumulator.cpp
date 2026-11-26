//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/axisaccumulator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/axisaccumulator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/axisaccumulator_p.h>
#include <Qt3DInput/qaxis.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qaxisaccumulator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/axisaccumulator.cpp, line 15, as _ZN9Qt3DInput5Input15AxisAccumulatorC1Ev
namespace Qt3DInput::Input {
inline AxisAccumulator::AxisAccumulator()
    : BackendNode(ReadWrite)
    , m_sourceAxisId()
    , m_sourceAxisType(QAxisAccumulator::Velocity)
    , m_scale(1.0f)
    , m_value(0.0f)
    , m_velocity(0.0f)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axisaccumulator.cpp, line 25, as _ZN9Qt3DInput5Input15AxisAccumulator7cleanupEv
namespace Qt3DInput::Input {
inline void AxisAccumulator::cleanup()
{
    QBackendNode::setEnabled(false);
    m_sourceAxisId = Qt3DCore::QNodeId();
    m_sourceAxisType = QAxisAccumulator::Velocity;
    m_scale = 1.0f;
    m_value = 0.0f;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axisaccumulator.cpp, line 34, as _ZN9Qt3DInput5Input15AxisAccumulator8setValueEf
namespace Qt3DInput::Input {
inline void AxisAccumulator::setValue(float value)
{
    if (isEnabled() && value != m_value)
        m_value = value;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axisaccumulator.cpp, line 40, as _ZN9Qt3DInput5Input15AxisAccumulator11setVelocityEf
namespace Qt3DInput::Input {
inline void AxisAccumulator::setVelocity(float velocity)
{
    if (isEnabled() && velocity != m_velocity)
        m_velocity = velocity;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axisaccumulator.cpp, line 46, as _ZN9Qt3DInput5Input15AxisAccumulator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void AxisAccumulator::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QAxisAccumulator *node = qobject_cast<const QAxisAccumulator *>(frontEnd);
    if (!node)
        return;

    m_sourceAxisId = Qt3DCore::qIdForNode(node->sourceAxis());
    m_sourceAxisType = node->sourceAxisType();
    m_scale = node->scale();

    if (firstTime) {
        m_value = 0.f;
        m_velocity = 0.f;
    }
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axisaccumulator.cpp, line 63, as _ZN9Qt3DInput5Input15AxisAccumulator15stepIntegrationEPNS0_11AxisManagerEf
namespace Qt3DInput::Input {
inline void AxisAccumulator::stepIntegration(AxisManager *axisManager, float dt)
{
    Axis *sourceAxis = axisManager->lookupResource(m_sourceAxisId);
    if (!sourceAxis)
        return;

    const float axisValue = sourceAxis->axisValue();
    float newVelocity = 0.0f;
    float newValue = 0.0f;
    switch (m_sourceAxisType) {
    case QAxisAccumulator::Velocity:
        newVelocity = axisValue * m_scale;
        newValue = m_value + newVelocity * dt;
        break;

    case QAxisAccumulator::Acceleration:
        newVelocity = m_velocity + axisValue * m_scale * dt;
        newValue = m_value + newVelocity * dt;
        break;
    }
    setVelocity(newVelocity);
    setValue(newValue);
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::AxisAccumulator::AxisAccumulator()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AxisAccumulator *ritual_ZN9Qt3DInput5Input15AxisAccumulatorC1Ev() {
  return new Qt3DInput::Input::AxisAccumulator();
}

//  void Qt3DInput::Input::AxisAccumulator::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15AxisAccumulator7cleanupEv(
    Qt3DInput::Input::AxisAccumulator *self) {
  self->cleanup();
}

//  Qt3DCore::QNodeId Qt3DInput::Input::AxisAccumulator::sourceAxisId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK9Qt3DInput5Input15AxisAccumulator12sourceAxisIdEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return new Qt3DCore::QNodeId(self->sourceAxisId());
}

//  QAxisAccumulator::SourceAxisType
//      Qt3DInput::Input::AxisAccumulator::sourceAxisType() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisAccumulator::SourceAxisType ritual_ZNK9Qt3DInput5Input15AxisAccumulator14sourceAxisTypeEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return self->sourceAxisType();
}

//  float Qt3DInput::Input::AxisAccumulator::scale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15AxisAccumulator5scaleEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return self->scale();
}

//  float Qt3DInput::Input::AxisAccumulator::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15AxisAccumulator5valueEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return self->value();
}

//  void Qt3DInput::Input::AxisAccumulator::setValue(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15AxisAccumulator8setValueEf(
    Qt3DInput::Input::AxisAccumulator *self,
    float value) {
  self->setValue(value);
}

//  float Qt3DInput::Input::AxisAccumulator::velocity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15AxisAccumulator8velocityEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return self->velocity();
}

//  void Qt3DInput::Input::AxisAccumulator::setVelocity(float velocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15AxisAccumulator11setVelocityEf(
    Qt3DInput::Input::AxisAccumulator *self,
    float velocity) {
  self->setVelocity(velocity);
}

//  void Qt3DInput::Input::AxisAccumulator::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15AxisAccumulator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::AxisAccumulator *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::AxisAccumulator::stepIntegration(AxisManager
//      *axisManager, float dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15AxisAccumulator15stepIntegrationEPNS0_11AxisManagerEf(
    Qt3DInput::Input::AxisAccumulator *self,
    Qt3DInput::Input::AxisManager *axisManager,
    float dt) {
  self->stepIntegration(axisManager, dt);
}

//  void Qt3DInput::Input::AxisAccumulator::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input15AxisAccumulator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::AxisAccumulator *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::AxisAccumulator::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
