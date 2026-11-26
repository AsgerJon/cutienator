//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/keyboardhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/keyboardhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/keyboarddevice_p.h>
#include <Qt3DInput/QKeyEvent>
#include <Qt3DCore/qnode.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/keyboardhandler_p.h>
#include <Qt3DInput/qkeyboarddevice.h>
#include <Qt3DInput/qkeyboardhandler.h>
#include <QtCore/QVariant>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qkeyboardhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 345, as _ZN9Qt3DInput5Input14KeyboardDevice20requestFocusForInputEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline void KeyboardDevice::requestFocusForInput(Qt3DCore::QNodeId inputId)
{
    // Saves the last inputId, this will then be used in an Aspect Job to determine which
    // input will have the focus. This in turn will call KeyboardInput::setFocus which will
    // decide if sending a notification to the frontend is necessary
    m_lastRequester = inputId;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 22, as _ZN9Qt3DInput5Input15KeyboardHandlerC1Ev
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline KeyboardHandler::KeyboardHandler()
    : BackendNode(QBackendNode::ReadWrite)
    , m_inputHandler(nullptr)
    , m_focus(false)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 29, as _ZNK9Qt3DInput5Input15KeyboardHandler14keyboardDeviceEv
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline Qt3DCore::QNodeId KeyboardHandler::keyboardDevice() const
{
    return m_keyboardDevice;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 34, as _ZN9Qt3DInput5Input15KeyboardHandler15setInputHandlerEPNS0_12InputHandlerE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void KeyboardHandler::setInputHandler(InputHandler *handler)
{
    m_inputHandler = handler;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 41, as _ZN9Qt3DInput5Input15KeyboardHandler8setFocusEb
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void KeyboardHandler::setFocus(bool focus)
{
    if (focus != m_focus)
        m_focus = focus;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 47, as _ZN9Qt3DInput5Input15KeyboardHandler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void KeyboardHandler::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QKeyboardHandler *node = qobject_cast<const Qt3DInput::QKeyboardHandler *>(frontEnd);
    if (!node)
        return;

    if (firstTime)
        m_focus = false;

    bool focusRequest = false;
    auto id = Qt3DCore::qIdForNode(node->sourceDevice());
    if (m_keyboardDevice != id) {
        setSourcerDevice(id);
        focusRequest = m_focus;
    }

    if (m_focus != node->focus())
        focusRequest = node->focus();

    if (focusRequest)
        requestFocus();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 71, as _ZN9Qt3DInput5Input15KeyboardHandler12requestFocusEv
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void KeyboardHandler::requestFocus()
{
    KeyboardDevice *keyboardDevice = m_inputHandler->keyboardDeviceManager()->lookupResource(m_keyboardDevice);
    if (keyboardDevice && isEnabled())
        keyboardDevice->requestFocusForInput(peerId());
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 78, as _ZN9Qt3DInput5Input15KeyboardHandler16setSourcerDeviceEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void KeyboardHandler::setSourcerDevice(QNodeId device)
{
    m_keyboardDevice = device;
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::KeyboardHandler::KeyboardHandler()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::KeyboardHandler *ritual_ZN9Qt3DInput5Input15KeyboardHandlerC1Ev() {
  return new Qt3DInput::Input::KeyboardHandler();
}

//  Qt3DCore::QNodeId Qt3DInput::Input::KeyboardHandler::keyboardDevice()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK9Qt3DInput5Input15KeyboardHandler14keyboardDeviceEv(
    const Qt3DInput::Input::KeyboardHandler *self) {
  return new Qt3DCore::QNodeId(self->keyboardDevice());
}

//  void Qt3DInput::Input::KeyboardHandler::setInputHandler(InputHandler
//      *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15KeyboardHandler15setInputHandlerEPNS0_12InputHandlerE(
    Qt3DInput::Input::KeyboardHandler *self,
    Qt3DInput::Input::InputHandler *handler) {
  self->setInputHandler(handler);
}

//  void Qt3DInput::Input::KeyboardHandler::setFocus(bool focus)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15KeyboardHandler8setFocusEb(
    Qt3DInput::Input::KeyboardHandler *self,
    bool focus) {
  self->setFocus(focus);
}

//  bool Qt3DInput::Input::KeyboardHandler::focus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput5Input15KeyboardHandler5focusEv(
    const Qt3DInput::Input::KeyboardHandler *self) {
  return self->focus();
}

//  void Qt3DInput::Input::KeyboardHandler::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15KeyboardHandler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::KeyboardHandler *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::KeyboardHandler::requestFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15KeyboardHandler12requestFocusEv(
    Qt3DInput::Input::KeyboardHandler *self) {
  self->requestFocus();
}

//  void
//      Qt3DInput::Input::KeyboardHandler::setSourcerDevice(Qt3DCore::QNodeId
//      device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15KeyboardHandler16setSourcerDeviceEN8Qt3DCore7QNodeIdE(
    Qt3DInput::Input::KeyboardHandler *self,
    const Qt3DCore::QNodeId *device) {
  self->setSourcerDevice(*device);
}

//  void Qt3DInput::Input::KeyboardHandler::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input15KeyboardHandler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::KeyboardHandler *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::KeyboardHandler::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
