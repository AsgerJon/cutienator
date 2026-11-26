//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/buttonaxisinput_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/buttonaxisinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/buttonaxisinput_p.h>
#include <Qt3DInput/qbuttonaxisinput.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/qabstractphysicaldevicebackendnode_p.h>
#include <Qt3DInput/private/qbuttonaxisinput_p.h>
#include <Qt3DInput/private/utils_p.h>
#include <Qt3DInput/qabstractaxisinput.h>
#include <Qt3DInput/private/qabstractaxisinput_p.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/abstractaxisinput_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qinputdeviceintegration_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DInput/qmousehandler.h>
#include <Qt3DInput/qkeyboardhandler.h>
#include <Qt3DInput/private/assignkeyboardfocusjob_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/inputsettings_p.h>
#include <Qt3DInput/private/qinputdeviceintegration_p.h>
#include <Qt3DInput/private/qmousehandler_p.h>
#include <Qt3DInput/private/qkeyboardhandler_p.h>
#include <Qt3DCore/private/qeventfilterservice_p.h>
#include <Qt3DInput/private/physicaldeviceproxy_p.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <QtCore/QCoreApplication>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qabstractphysicaldeviceproxy_p.h>
#include <Qt3DInput/private/qabstractphysicaldeviceproxy_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/buttonaxisinput.cpp, line 71, as local:buttonaxisinput.cpp:anyOfRequiredButtonsPressed
namespace Qt3DInput::Input {
namespace {
inline bool anyOfRequiredButtonsPressed(const QList<int> &buttons, QAbstractPhysicalDeviceBackendNode *physicalDeviceBackend)
{
    bool validButtonWasPressed = false;
    for (int button : buttons) {
        if (physicalDeviceBackend->isButtonPressed(button)) {
            validButtonWasPressed = true;
            break;
        }
    }
    return validButtonWasPressed;
}
}  // namespace
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/buttonaxisinput.cpp, line 85, as _ZN9Qt3DInput5Input15ButtonAxisInput7processEPNS0_12InputHandlerEx
namespace Qt3DInput::Input {
inline float ButtonAxisInput::process(InputHandler *inputHandler, qint64 currentTime)
{
    if (!isEnabled())
        return 0.0f;

    if (m_buttons.isEmpty())
        return 0.0f;

    QAbstractPhysicalDeviceBackendNode *physicalDeviceBackend = Utils::physicalDeviceForInput(this, inputHandler);
    if (!physicalDeviceBackend)
        return 0.0f;

    // TO DO: Linear Curver for the progression of the scale value
    if (anyOfRequiredButtonsPressed(m_buttons, physicalDeviceBackend))
        updateSpeedRatio(currentTime, ButtonAxisInput::Accelerate);
    else if (m_speedRatio != 0.0f)
        updateSpeedRatio(currentTime, ButtonAxisInput::Decelerate);

    return m_speedRatio * m_scale;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/abstractaxisinput.cpp, line 30, as _ZN9Qt3DInput5Input17AbstractAxisInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void AbstractAxisInput::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QAbstractAxisInput *node = qobject_cast<const QAbstractAxisInput *>(frontEnd);
    if (!node)
        return;

    m_sourceDevice = Qt3DCore::qIdForNode(node->sourceDevice());
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/abstractaxisinput.cpp, line 24, as _ZN9Qt3DInput5Input17AbstractAxisInput7cleanupEv
namespace Qt3DInput::Input {
inline void AbstractAxisInput::cleanup()
{
    QBackendNode::setEnabled(false);
    m_sourceDevice = Qt3DCore::QNodeId();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/abstractaxisinput.cpp, line 19, as _ZN9Qt3DInput5Input17AbstractAxisInputC2Ev
namespace Qt3DInput::Input {
inline AbstractAxisInput::AbstractAxisInput()
    : BackendNode()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 206, as _ZNK9Qt3DInput5Input12InputHandler23inputDeviceIntegrationsEv
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline QList<QInputDeviceIntegration *> InputHandler::inputDeviceIntegrations() const
{
    return m_inputDeviceIntegrations;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 58, as _ZNK9Qt3DInput5Input19PhysicalDeviceProxy16physicalDeviceIdEv
namespace Qt3DInput::Input {
inline Qt3DCore::QNodeId PhysicalDeviceProxy::physicalDeviceId() const
{
    return m_physicalDeviceId;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/buttonaxisinput.cpp, line 29, as _ZN9Qt3DInput5Input15ButtonAxisInput7cleanupEv
namespace Qt3DInput::Input {
inline void ButtonAxisInput::cleanup()
{
    m_scale = 0.0f;
    m_buttons.clear();
    m_acceleration = -1.0f;
    m_deceleration = -1.0f;
    AbstractAxisInput::cleanup();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/buttonaxisinput.cpp, line 56, as _ZN9Qt3DInput5Input15ButtonAxisInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void ButtonAxisInput::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    AbstractAxisInput::syncFromFrontEnd(frontEnd, firstTime);
    const QButtonAxisInput *node = qobject_cast<const QButtonAxisInput *>(frontEnd);
    if (!node)
        return;

    m_scale = node->scale();
    m_buttons = node->buttons();
    m_acceleration = node->acceleration();
    m_deceleration = node->deceleration();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/buttonaxisinput.cpp, line 38, as _ZN9Qt3DInput5Input15ButtonAxisInput16updateSpeedRatioExNS1_10UpdateTypeE
namespace Qt3DInput::Input {
inline void ButtonAxisInput::updateSpeedRatio(qint64 currentTime, ButtonAxisInput::UpdateType type)
{
    const float accel = (type == Accelerate) ? acceleration() : -deceleration();

    // Was in nanoseconds, while acceleration will be in units per square seconds
    const float delta = m_lastUpdateTime ? (currentTime - m_lastUpdateTime) / 1000000000.0f : 0.0f;
    const float speedRatio = m_speedRatio + delta * accel;

    // Clamp it
    m_speedRatio = qMax(0.0f, qMin(speedRatio, 1.0f));

    // If we stopped, time to start over
    if (type == Decelerate && m_speedRatio == 0.0f)
        m_lastUpdateTime = 0;
    else
        m_lastUpdateTime = currentTime;
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  void Qt3DInput::Input::ButtonAxisInput::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15ButtonAxisInput7cleanupEv(
    Qt3DInput::Input::ButtonAxisInput *self) {
  self->cleanup();
}

//  float Qt3DInput::Input::ButtonAxisInput::scale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15ButtonAxisInput5scaleEv(
    const Qt3DInput::Input::ButtonAxisInput *self) {
  return self->scale();
}

//  QList<int> Qt3DInput::Input::ButtonAxisInput::buttons() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK9Qt3DInput5Input15ButtonAxisInput7buttonsEv(
    const Qt3DInput::Input::ButtonAxisInput *self) {
  return new QList<int>(self->buttons());
}

//  float Qt3DInput::Input::ButtonAxisInput::acceleration() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15ButtonAxisInput12accelerationEv(
    const Qt3DInput::Input::ButtonAxisInput *self) {
  return self->acceleration();
}

//  float Qt3DInput::Input::ButtonAxisInput::deceleration() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15ButtonAxisInput12decelerationEv(
    const Qt3DInput::Input::ButtonAxisInput *self) {
  return self->deceleration();
}

//  float Qt3DInput::Input::ButtonAxisInput::speedRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15ButtonAxisInput10speedRatioEv(
    const Qt3DInput::Input::ButtonAxisInput *self) {
  return self->speedRatio();
}

//  qint64 Qt3DInput::Input::ButtonAxisInput::lastUpdateTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9Qt3DInput5Input15ButtonAxisInput14lastUpdateTimeEv(
    const Qt3DInput::Input::ButtonAxisInput *self) {
  return self->lastUpdateTime();
}

//  void Qt3DInput::Input::ButtonAxisInput::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15ButtonAxisInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::ButtonAxisInput *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  float Qt3DInput::Input::ButtonAxisInput::process(InputHandler
//      *inputHandler, qint64 currentTime)
extern "C" Q_DECL_EXPORT
float ritual_ZN9Qt3DInput5Input15ButtonAxisInput7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::ButtonAxisInput *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->process(inputHandler, currentTime);
}

//  void Qt3DInput::Input::ButtonAxisInput::updateSpeedRatio(qint64
//      currentTime, UpdateType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15ButtonAxisInput16updateSpeedRatioExNS1_10UpdateTypeE(
    Qt3DInput::Input::ButtonAxisInput *self,
    qint64 currentTime,
    Qt3DInput::Input::ButtonAxisInput::UpdateType type) {
  self->updateSpeedRatio(currentTime, type);
}

//  float Qt3DInput::Input::ButtonAxisInput::process(InputHandler
//      *inputHandler, qint64 currentTime)
extern "C" Q_DECL_EXPORT
float ritual_own_ZN9Qt3DInput5Input15ButtonAxisInput7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::ButtonAxisInput *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->Qt3DInput::Input::ButtonAxisInput::process(
      inputHandler,
      currentTime);
}

//  a QList<int> a ritual of Qt3DInput::Input::ButtonAxisInput gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_ButtonAxisInput__QList_int(
    QList<int> *self) {
  delete self;
}
