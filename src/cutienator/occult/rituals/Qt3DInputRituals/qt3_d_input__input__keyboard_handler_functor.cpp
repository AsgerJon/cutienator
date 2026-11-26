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
#include <Qt3DInput/private/keyboardhandler_p.h>
#include <Qt3DInput/qkeyboarddevice.h>
#include <Qt3DInput/qkeyboardhandler.h>
#include <QtCore/QVariant>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qkeyboardhandler_p.h>
#include <Qt3DInput/private/keyboarddevice_p.h>
#include <Qt3DInput/QKeyEvent>
#include <Qt3DCore/qnode.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 88, as _ZNK9Qt3DInput5Input22KeyboardHandlerFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *KeyboardHandlerFunctor::create(Qt3DCore::QNodeId id) const
{
    KeyboardHandler *input = m_handler->keyboardInputManager()->getOrCreateResource(id);
    input->setInputHandler(m_handler);
    return input;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 95, as _ZNK9Qt3DInput5Input22KeyboardHandlerFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline QBackendNode *KeyboardHandlerFunctor::get(QNodeId id) const
{
    return m_handler->keyboardInputManager()->lookupResource(id);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 100, as _ZNK9Qt3DInput5Input22KeyboardHandlerFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void KeyboardHandlerFunctor::destroy(QNodeId id) const
{
    m_handler->keyboardInputManager()->releaseResource(id);
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

//  from ../qt3d/src/input/backend/keyboardhandler.cpp, line 83, as _ZN9Qt3DInput5Input22KeyboardHandlerFunctorC1EPNS0_12InputHandlerE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline KeyboardHandlerFunctor::KeyboardHandlerFunctor(InputHandler *handler)
    : m_handler(handler)
{
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::KeyboardHandlerFunctor::KeyboardHandlerFunctor(InputHan
//      dler *handler)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::KeyboardHandlerFunctor *ritual_ZN9Qt3DInput5Input22KeyboardHandlerFunctorC1EPNS0_12InputHandlerE(
    Qt3DInput::Input::InputHandler *handler) {
  return new Qt3DInput::Input::KeyboardHandlerFunctor(handler);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::KeyboardHandlerFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input22KeyboardHandlerFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::KeyboardHandlerFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input22KeyboardHandlerFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DInput::Input::KeyboardHandlerFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9Qt3DInput5Input22KeyboardHandlerFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DInput::Input::KeyboardHandlerFunctor::~KeyboardHandlerFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input22KeyboardHandlerFunctorD1Ev(
    Qt3DInput::Input::KeyboardHandlerFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::KeyboardHandlerFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DInput5Input22KeyboardHandlerFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DInput::Input::KeyboardHandlerFunctor::get(*id);
}

//  void Qt3DInput::Input::KeyboardHandlerFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9Qt3DInput5Input22KeyboardHandlerFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DInput::Input::KeyboardHandlerFunctor::destroy(*id);
}
