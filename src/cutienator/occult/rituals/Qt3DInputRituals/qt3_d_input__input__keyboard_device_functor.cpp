//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/keyboarddevice_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/keyboarddevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/keyboarddevice_p.h>
#include <Qt3DInput/QKeyEvent>
#include <Qt3DCore/qnode.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
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

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 20, as local:keyboarddevice.cpp:getKeyPosition
namespace Qt3DInput::Input {
namespace {
inline QPair<int, int> getKeyPosition(int key)
{
    QPair<int, int> position;

    switch (key) {
    case Qt::Key_Escape:
        return QPair<int, int>(0, 0);
    case Qt::Key_Tab:
        return QPair<int, int>(0, 1);
    case Qt::Key_Backtab:
        return QPair<int, int>(0, 2);
    case Qt::Key_Backspace:
        return QPair<int, int>(0, 3);
    case Qt::Key_Return:
        return QPair<int, int>(0, 4);
    case Qt::Key_Enter:
        return QPair<int, int>(0, 5);
    case Qt::Key_Insert:
        return QPair<int, int>(0, 6);
    case Qt::Key_Delete:
        return QPair<int, int>(0, 7);
    case Qt::Key_Pause:
        return QPair<int, int>(0, 8);
    case Qt::Key_Print:
        return QPair<int, int>(0, 9);
    case Qt::Key_SysReq:
        return QPair<int, int>(0, 10);
    case Qt::Key_Clear:
        return QPair<int, int>(0, 11);
    case Qt::Key_Home:
        return QPair<int, int>(0, 12);
    case Qt::Key_End:
        return QPair<int, int>(0, 13);
    case Qt::Key_Left:
        return QPair<int, int>(0, 14);
    case Qt::Key_Right:
        return QPair<int, int>(0, 16);
    case Qt::Key_Up:
        return QPair<int, int>(0, 15);
    case Qt::Key_Down:
        return QPair<int, int>(0, 17);
    case Qt::Key_PageUp:
        return QPair<int, int>(0, 18);
    case Qt::Key_PageDown:
        return QPair<int, int>(0, 19);
    case Qt::Key_Shift:
        return QPair<int, int>(0, 20);
    case Qt::Key_Alt:
        return QPair<int, int>(0, 23);
    case Qt::Key_Control:
        return QPair<int, int>(0, 21);
    case Qt::Key_Meta:
        return QPair<int, int>(0, 22);
    case Qt::Key_CapsLock:
        return QPair<int, int>(0, 24);
    case Qt::Key_NumLock:
        return QPair<int, int>(0, 25);
    case Qt::Key_ScrollLock:
        return QPair<int, int>(0, 26);
    case Qt::Key_F1:
        return QPair<int, int>(0, 27);
    case Qt::Key_F2:
        return QPair<int, int>(0, 28);
    case Qt::Key_F3:
        return QPair<int, int>(0, 29);
    case Qt::Key_F4:
        return QPair<int, int>(0, 30);
    case Qt::Key_F5:
        return QPair<int, int>(0, 31);
    case Qt::Key_F6:
        return QPair<int, int>(1, 0);
    case Qt::Key_F7:
        return QPair<int, int>(1, 1);
    case Qt::Key_F8:
        return QPair<int, int>(1, 2);
    case Qt::Key_F9:
        return QPair<int, int>(1, 3);
    case Qt::Key_F10:
        return QPair<int, int>(1, 4);
    case Qt::Key_F11:
        return QPair<int, int>(1, 5);
    case Qt::Key_F12:
        return QPair<int, int>(1, 6);
    case Qt::Key_F13:
        return QPair<int, int>(1, 7);
    case Qt::Key_F14:
        return QPair<int, int>(1, 8);
    case Qt::Key_F15:
        return QPair<int, int>(1, 9);
    case Qt::Key_F16:
        return QPair<int, int>(1, 10);
    case Qt::Key_F17:
        return QPair<int, int>(1, 11);
    case Qt::Key_F18:
        return QPair<int, int>(1, 12);
    case Qt::Key_F19:
        return QPair<int, int>(1, 13);
    case Qt::Key_F20:
        return QPair<int, int>(1, 14);
    case Qt::Key_F21:
        return QPair<int, int>(1, 15);
    case Qt::Key_F22:
        return QPair<int, int>(1, 16);
    case Qt::Key_F23:
        return QPair<int, int>(1, 17);
    case Qt::Key_F24:
        return QPair<int, int>(1, 18);
    case Qt::Key_F25:
        return QPair<int, int>(1, 19);
    case Qt::Key_F26:
        return QPair<int, int>(1, 20);
    case Qt::Key_F27:
        return QPair<int, int>(1, 21);
    case Qt::Key_F28:
        return QPair<int, int>(1, 22);
    case Qt::Key_F29:
        return QPair<int, int>(1, 23);
    case Qt::Key_F30:
        return QPair<int, int>(1, 24);
    case Qt::Key_F31:
        return QPair<int, int>(1, 25);
    case Qt::Key_F32:
        return QPair<int, int>(1, 26);
    case Qt::Key_F33:
        return QPair<int, int>(1, 27);
    case Qt::Key_F34:
        return QPair<int, int>(1, 28);
    case Qt::Key_F35:
        return QPair<int, int>(1, 29);
    case Qt::Key_Super_L:
        return QPair<int, int>(1, 30);
    case Qt::Key_Super_R:
        return QPair<int, int>(1, 31);
    case Qt::Key_Menu:
        return QPair<int, int>(2, 1);
    case Qt::Key_Help:
        return QPair<int, int>(2, 4);
    case Qt::Key_Hyper_L:
        return QPair<int, int>(2, 2);
    case Qt::Key_Hyper_R:
        return QPair<int, int>(2, 3);
    case Qt::Key_Direction_L:
        return QPair<int, int>(2, 5);
    case Qt::Key_Direction_R:
        return QPair<int, int>(2, 6);
    case Qt::Key_Space:
        return QPair<int, int>(2, 7);
    case Qt::Key_Exclam:
        return QPair<int, int>(2, 9);
    case Qt::Key_QuoteDbl:
        return QPair<int, int>(2, 10);
    case Qt::Key_NumberSign:
        return QPair<int, int>(2, 11);
    case Qt::Key_Dollar:
        return QPair<int, int>(2, 12);
    case Qt::Key_Percent:
        return QPair<int, int>(2, 13);
    case Qt::Key_Ampersand:
        return QPair<int, int>(2, 14);
    case Qt::Key_Apostrophe:
        return QPair<int, int>(2, 15);
    case Qt::Key_ParenLeft:
        return QPair<int, int>(2, 16);
    case Qt::Key_ParenRight:
        return QPair<int, int>(2, 17);
    case Qt::Key_Asterisk:
        return QPair<int, int>(2, 18);
    case Qt::Key_Plus:
        return QPair<int, int>(2, 19);
    case Qt::Key_Comma:
        return QPair<int, int>(2, 20);
    case Qt::Key_Minus:
        return QPair<int, int>(2, 21);
    case Qt::Key_Period:
        return QPair<int, int>(2, 22);
    case Qt::Key_Slash:
        return QPair<int, int>(2, 23);
    case Qt::Key_0:
        return QPair<int, int>(2, 24);
    case Qt::Key_1:
        return QPair<int, int>(2, 25);
    case Qt::Key_2:
        return QPair<int, int>(2, 26);
    case Qt::Key_3:
        return QPair<int, int>(2, 27);
    case Qt::Key_4:
        return QPair<int, int>(2, 28);
    case Qt::Key_5:
        return QPair<int, int>(2, 29);
    case Qt::Key_6:
        return QPair<int, int>(2, 30);
    case Qt::Key_7:
        return QPair<int, int>(2, 31);
    case Qt::Key_8:
        return QPair<int, int>(3, 0);
    case Qt::Key_9:
        return QPair<int, int>(3, 1);
    case Qt::Key_Colon:
        return QPair<int, int>(3, 2);
    case Qt::Key_Semicolon:
        return QPair<int, int>(3, 3);
    case Qt::Key_Less:
        return QPair<int, int>(3, 4);
    case Qt::Key_Equal:
        return QPair<int, int>(3, 5);
    case Qt::Key_Greater:
        return QPair<int, int>(3, 6);
    case Qt::Key_Question:
        return QPair<int, int>(3, 7);
    case Qt::Key_At:
        return QPair<int, int>(3, 8);
    case Qt::Key_A:
        return QPair<int, int>(3, 9);
    case Qt::Key_B:
        return QPair<int, int>(3, 10);
    case Qt::Key_C:
        return QPair<int, int>(3, 11);
    case Qt::Key_D:
        return QPair<int, int>(3, 12);
    case Qt::Key_E:
        return QPair<int, int>(3, 13);
    case Qt::Key_F:
        return QPair<int, int>(3, 14);
    case Qt::Key_G:
        return QPair<int, int>(3, 15);
    case Qt::Key_H:
        return QPair<int, int>(3, 16);
    case Qt::Key_I:
        return QPair<int, int>(3, 17);
    case Qt::Key_J:
        return QPair<int, int>(3, 18);
    case Qt::Key_K:
        return QPair<int, int>(3, 19);
    case Qt::Key_L:
        return QPair<int, int>(3, 20);
    case Qt::Key_M:
        return QPair<int, int>(3, 21);
    case Qt::Key_N:
        return QPair<int, int>(3, 22);
    case Qt::Key_O:
        return QPair<int, int>(3, 23);
    case Qt::Key_P:
        return QPair<int, int>(3, 24);
    case Qt::Key_Q:
        return QPair<int, int>(3, 25);
    case Qt::Key_R:
        return QPair<int, int>(3, 26);
    case Qt::Key_S:
        return QPair<int, int>(3, 27);
    case Qt::Key_T:
        return QPair<int, int>(3, 28);
    case Qt::Key_U:
        return QPair<int, int>(3, 29);
    case Qt::Key_V:
        return QPair<int, int>(3, 30);
    case Qt::Key_W:
        return QPair<int, int>(3, 31);
    case Qt::Key_X:
        return QPair<int, int>(4, 0);
    case Qt::Key_Y:
        return QPair<int, int>(4, 1);
    case Qt::Key_Z:
        return QPair<int, int>(4, 2);
    case Qt::Key_BracketLeft:
        return QPair<int, int>(4, 3);
    case Qt::Key_Backslash:
        return QPair<int, int>(4, 4);
    case Qt::Key_BracketRight:
        return QPair<int, int>(4, 5);
    case Qt::Key_AsciiCircum:
        return QPair<int, int>(4, 6);
    case Qt::Key_Underscore:
        return QPair<int, int>(4, 7);
    case Qt::Key_QuoteLeft:
        return QPair<int, int>(4, 8);
    case Qt::Key_BraceLeft:
        return QPair<int, int>(4, 9);
    case Qt::Key_Bar:
        return QPair<int, int>(4, 10);
    case Qt::Key_BraceRight:
        return QPair<int, int>(4, 11);
    case Qt::Key_AsciiTilde:
        return QPair<int, int>(4, 12);
    case Qt::Key_plusminus:
        return QPair<int, int>(4, 13);
    case Qt::Key_onesuperior:
        return QPair<int, int>(4, 14);
    case Qt::Key_multiply:
        return QPair<int, int>(4, 15);
    case Qt::Key_division:
        return QPair<int, int>(4, 16);
    case Qt::Key_diaeresis:
        return QPair<int, int>(4, 17);
    default:
        return QPair<int, int>(-1, -1);
    }
    return position;
}
}  // namespace
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 399, as _ZNK9Qt3DInput5Input21KeyboardDeviceFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *KeyboardDeviceFunctor::create(Qt3DCore::QNodeId id) const
{
    KeyboardDevice *keyboardDevice = m_handler->keyboardDeviceManager()->getOrCreateResource(id);
    keyboardDevice->setInputAspect(m_inputAspect);
    keyboardDevice->setInputHandler(m_handler);
    m_handler->appendKeyboardDevice(m_handler->keyboardDeviceManager()->lookupHandle(id));
    return keyboardDevice;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 408, as _ZNK9Qt3DInput5Input21KeyboardDeviceFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *KeyboardDeviceFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_handler->keyboardDeviceManager()->lookupResource(id);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 413, as _ZNK9Qt3DInput5Input21KeyboardDeviceFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline void KeyboardDeviceFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_handler->removeKeyboardDevice(m_handler->keyboardDeviceManager()->lookupHandle(id));
    m_handler->keyboardDeviceManager()->releaseResource(id);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 167, as _ZN9Qt3DInput5Input12InputHandler20appendKeyboardDeviceEN8Qt3DCore7QHandleINS0_14KeyboardDeviceEEE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::appendKeyboardDevice(HKeyboardDevice device)
{
    m_activeKeyboardDevices.append(device);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 172, as _ZN9Qt3DInput5Input12InputHandler20removeKeyboardDeviceEN8Qt3DCore7QHandleINS0_14KeyboardDeviceEEE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::removeKeyboardDevice(HKeyboardDevice device)
{
    m_activeKeyboardDevices.removeAll(device);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 353, as _ZN9Qt3DInput5Input14KeyboardDevice15setInputHandlerEPNS0_12InputHandlerE
namespace Qt3DInput::Input {
inline void KeyboardDevice::setInputHandler(InputHandler *handler)
{
    m_inputHandler = handler;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 324, as _ZN9Qt3DInput5Input14KeyboardDeviceC1Ev
namespace Qt3DInput::Input {
inline KeyboardDevice::KeyboardDevice()
    : QAbstractPhysicalDeviceBackendNode(QBackendNode::ReadOnly)
    , m_inputHandler(nullptr)
{
    m_keyStates.keys[0] = 0;
    m_keyStates.keys[1] = 0;
    m_keyStates.keys[2] = 0;
    m_keyStates.keys[3] = 0;
    m_keyStates.keys[4] = 0;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 335, as _ZN9Qt3DInput5Input14KeyboardDevice7cleanupEv
namespace Qt3DInput::Input {
inline void KeyboardDevice::cleanup()
{
    QAbstractPhysicalDeviceBackendNode::cleanup();
    m_keyStates.keys[0] = 0;
    m_keyStates.keys[1] = 0;
    m_keyStates.keys[2] = 0;
    m_keyStates.keys[3] = 0;
    m_keyStates.keys[4] = 0;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 363, as _ZNK9Qt3DInput5Input14KeyboardDevice9axisValueEi
namespace Qt3DInput::Input {
inline float KeyboardDevice::axisValue(int axisIdentifier) const
{
    Q_UNUSED(axisIdentifier);
    return 0.0f;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 369, as _ZNK9Qt3DInput5Input14KeyboardDevice15isButtonPressedEi
namespace Qt3DInput::Input {
inline bool KeyboardDevice::isButtonPressed(int buttonIdentifier) const
{
    QPair<int, int> position = getKeyPosition(buttonIdentifier);
    if (position.first != -1 && position.second != -1)
        return m_keyStates.keys[position.first] & (1 << position.second);
    return false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 393, as _ZN9Qt3DInput5Input21KeyboardDeviceFunctorC1EPNS_12QInputAspectEPNS0_12InputHandlerE
namespace Qt3DInput::Input {
inline KeyboardDeviceFunctor::KeyboardDeviceFunctor(QInputAspect *inputaspect, InputHandler *handler)
    : m_inputAspect(inputaspect)
    , m_handler(handler)
{
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::KeyboardDeviceFunctor::KeyboardDeviceFunctor(QInputAspe
//      ct *inputaspect, InputHandler *handler)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::KeyboardDeviceFunctor *ritual_ZN9Qt3DInput5Input21KeyboardDeviceFunctorC1EPNS_12QInputAspectEPNS0_12InputHandlerE(
    Qt3DInput::QInputAspect *inputaspect,
    Qt3DInput::Input::InputHandler *handler) {
  return new Qt3DInput::Input::KeyboardDeviceFunctor(inputaspect, handler);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::KeyboardDeviceFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input21KeyboardDeviceFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::KeyboardDeviceFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input21KeyboardDeviceFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DInput::Input::KeyboardDeviceFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9Qt3DInput5Input21KeyboardDeviceFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DInput::Input::KeyboardDeviceFunctor::~KeyboardDeviceFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input21KeyboardDeviceFunctorD1Ev(
    Qt3DInput::Input::KeyboardDeviceFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::KeyboardDeviceFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DInput5Input21KeyboardDeviceFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DInput::Input::KeyboardDeviceFunctor::get(*id);
}

//  void Qt3DInput::Input::KeyboardDeviceFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9Qt3DInput5Input21KeyboardDeviceFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardDeviceFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DInput::Input::KeyboardDeviceFunctor::destroy(*id);
}
