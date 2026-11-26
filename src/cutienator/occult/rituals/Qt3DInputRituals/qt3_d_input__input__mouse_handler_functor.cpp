//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/mousehandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/mousehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/mousehandler_p.h>
#include <Qt3DInput/qmousehandler.h>
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/mousedevice_p.h>
#include <Qt3DInput/private/qmousehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 37, as _ZN9Qt3DInput5Input12MouseHandler15setInputHandlerEPNS0_12InputHandlerE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void MouseHandler::setInputHandler(InputHandler *handler)
{
    m_inputHandler = handler;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 22, as _ZN9Qt3DInput5Input12MouseHandlerC1Ev
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline MouseHandler::MouseHandler()
    : BackendNode(ReadWrite)
    , m_inputHandler(nullptr)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 28, as _ZN9Qt3DInput5Input12MouseHandlerD1Ev
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline MouseHandler::~MouseHandler()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 42, as _ZN9Qt3DInput5Input12MouseHandler16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void MouseHandler::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QMouseHandler *node = qobject_cast<const Qt3DInput::QMouseHandler *>(frontEnd);
    if (!node)
        return;

    const auto newId = Qt3DCore::qIdForNode(node->sourceDevice());
    if (m_mouseDevice != newId)
        setDevice(newId);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 54, as _ZN9Qt3DInput5Input12MouseHandler9setDeviceEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void MouseHandler::setDevice(Qt3DCore::QNodeId device)
{
    m_mouseDevice = device;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 59, as _ZN9Qt3DInput5Input19MouseHandlerFunctorC1EPNS0_12InputHandlerE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline MouseHandlerFunctor::MouseHandlerFunctor(InputHandler *handler)
    : m_handler(handler)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 64, as _ZNK9Qt3DInput5Input19MouseHandlerFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *MouseHandlerFunctor::create(Qt3DCore::QNodeId id) const
{
    MouseHandler *input = m_handler->mouseInputManager()->getOrCreateResource(id);
    input->setInputHandler(m_handler);
    return input;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 71, as _ZNK9Qt3DInput5Input19MouseHandlerFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *MouseHandlerFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_handler->mouseInputManager()->lookupResource(id);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 76, as _ZNK9Qt3DInput5Input19MouseHandlerFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void MouseHandlerFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_handler->mouseInputManager()->releaseResource(id);
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::MouseHandlerFunctor::MouseHandlerFunctor(InputHandler
//      *handler)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MouseHandlerFunctor *ritual_ZN9Qt3DInput5Input19MouseHandlerFunctorC1EPNS0_12InputHandlerE(
    Qt3DInput::Input::InputHandler *handler) {
  return new Qt3DInput::Input::MouseHandlerFunctor(handler);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::MouseHandlerFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input19MouseHandlerFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::MouseHandlerFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input19MouseHandlerFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DInput::Input::MouseHandlerFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9Qt3DInput5Input19MouseHandlerFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DInput::Input::MouseHandlerFunctor::~MouseHandlerFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input19MouseHandlerFunctorD1Ev(
    Qt3DInput::Input::MouseHandlerFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::MouseHandlerFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DInput5Input19MouseHandlerFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DInput::Input::MouseHandlerFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::MouseHandlerFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DInput5Input19MouseHandlerFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DInput::Input::MouseHandlerFunctor::get(*id);
}

//  void Qt3DInput::Input::MouseHandlerFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9Qt3DInput5Input19MouseHandlerFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::MouseHandlerFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DInput::Input::MouseHandlerFunctor::destroy(*id);
}
