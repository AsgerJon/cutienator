//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/mousedevice_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/mousedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/mousedevice_p.h>
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qmousedevice_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 32, as _ZN9Qt3DInput5Input11MouseDevice15setInputHandlerEPNS0_12InputHandlerE
namespace Qt3DInput::Input {
inline void MouseDevice::setInputHandler(InputHandler *handler)
{
    m_inputHandler = handler;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 19, as _ZN9Qt3DInput5Input11MouseDeviceC1Ev
namespace Qt3DInput::Input {
inline MouseDevice::MouseDevice()
    : QAbstractPhysicalDeviceBackendNode(ReadOnly)
    , m_inputHandler(nullptr)
    , m_wasPressed(false)
    , m_sensitivity(0.1f)
    , m_updateAxesContinuously(false)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 28, as _ZN9Qt3DInput5Input11MouseDeviceD1Ev
namespace Qt3DInput::Input {
inline MouseDevice::~MouseDevice()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 177, as _ZN9Qt3DInput5Input12InputHandler17appendMouseDeviceEN8Qt3DCore7QHandleINS0_11MouseDeviceEEE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::appendMouseDevice(HMouseDevice device)
{
    m_activeMouseDevices.append(device);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 182, as _ZN9Qt3DInput5Input12InputHandler17removeMouseDeviceEN8Qt3DCore7QHandleINS0_11MouseDeviceEEE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::removeMouseDevice(HMouseDevice device)
{
    m_activeMouseDevices.removeAll(device);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 132, as _ZN9Qt3DInput5Input11MouseDevice16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void MouseDevice::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QMouseDevice *node = qobject_cast<const Qt3DInput::QMouseDevice *>(frontEnd);
    if (!node)
        return;

    m_sensitivity = node->sensitivity();
    m_updateAxesContinuously = node->updateAxesContinuously();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 59, as _ZNK9Qt3DInput5Input11MouseDevice15isButtonPressedEi
namespace Qt3DInput::Input {
inline bool MouseDevice::isButtonPressed(int buttonIdentifier) const
{
    switch (buttonIdentifier) {
    case QMouseEvent::LeftButton:
        return m_mouseState.leftPressed;
    case QMouseEvent::MiddleButton:
        return m_mouseState.centerPressed;
    case QMouseEvent::RightButton:
        return m_mouseState.rightPressed;
    default:
        break;
    }
    return false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 42, as _ZNK9Qt3DInput5Input11MouseDevice9axisValueEi
namespace Qt3DInput::Input {
inline float MouseDevice::axisValue(int axisIdentifier) const
{
    switch (axisIdentifier) {
    case QMouseDevice::X:
        return m_mouseState.xAxis;
    case QMouseDevice::Y:
        return m_mouseState.yAxis;
    case QMouseDevice::WheelX:
        return m_mouseState.wXAxis;
    case QMouseDevice::WheelY:
        return m_mouseState.wYAxis;
    default:
        break;
    }
    return 0.0f;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 143, as _ZN9Qt3DInput5Input18MouseDeviceFunctorC1EPNS_12QInputAspectEPNS0_12InputHandlerE
namespace Qt3DInput::Input {
inline MouseDeviceFunctor::MouseDeviceFunctor(QInputAspect *inputAspect, InputHandler *handler)
    : m_inputAspect(inputAspect)
    , m_handler(handler)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 149, as _ZNK9Qt3DInput5Input18MouseDeviceFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *MouseDeviceFunctor::create(Qt3DCore::QNodeId id) const
{
    MouseDevice *controller = m_handler->mouseDeviceManager()->getOrCreateResource(id);
    controller->setInputAspect(m_inputAspect);
    controller->setInputHandler(m_handler);
    m_handler->appendMouseDevice(m_handler->mouseDeviceManager()->lookupHandle(id));
    return controller;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 158, as _ZNK9Qt3DInput5Input18MouseDeviceFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *MouseDeviceFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_handler->mouseDeviceManager()->lookupResource(id);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 163, as _ZNK9Qt3DInput5Input18MouseDeviceFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline void MouseDeviceFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_handler->removeMouseDevice(m_handler->mouseDeviceManager()->lookupHandle(id));
    m_handler->mouseDeviceManager()->releaseResource(id);
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::MouseDeviceFunctor::MouseDeviceFunctor(Qt3DInput::QInpu
//      tAspect *inputAspect, InputHandler *handler)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MouseDeviceFunctor *ritual_ZN9Qt3DInput5Input18MouseDeviceFunctorC1EPNS_12QInputAspectEPNS0_12InputHandlerE(
    Qt3DInput::QInputAspect *inputAspect,
    Qt3DInput::Input::InputHandler *handler) {
  return new Qt3DInput::Input::MouseDeviceFunctor(inputAspect, handler);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::MouseDeviceFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input18MouseDeviceFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::MouseDeviceFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input18MouseDeviceFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DInput::Input::MouseDeviceFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9Qt3DInput5Input18MouseDeviceFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DInput::Input::MouseDeviceFunctor::~MouseDeviceFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input18MouseDeviceFunctorD1Ev(
    Qt3DInput::Input::MouseDeviceFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::MouseDeviceFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DInput5Input18MouseDeviceFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DInput::Input::MouseDeviceFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::MouseDeviceFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DInput5Input18MouseDeviceFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DInput::Input::MouseDeviceFunctor::get(*id);
}

//  void Qt3DInput::Input::MouseDeviceFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9Qt3DInput5Input18MouseDeviceFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DInput::Input::MouseDeviceFunctor::destroy(*id);
}
