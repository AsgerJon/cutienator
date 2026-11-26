//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/genericdevicebackendnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/genericdevicebackendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <Qt3DInput/private/genericdevicebackendnode_p.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qgenericinputdevice_p.h>
#include <Qt3DInput/private/qabstractphysicaldevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 187, as _ZN9Qt3DInput5Input12InputHandler19appendGenericDeviceEN8Qt3DCore7QHandleINS0_24GenericDeviceBackendNodeEEE
inline void Qt3DInput::Input::InputHandler::appendGenericDevice(HGenericDeviceBackendNode device)
{
    m_activeGenericPhysicalDevices.append(device);
}

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 192, as _ZN9Qt3DInput5Input12InputHandler19removeGenericDeviceEN8Qt3DCore7QHandleINS0_24GenericDeviceBackendNodeEEE
inline void Qt3DInput::Input::InputHandler::removeGenericDevice(HGenericDeviceBackendNode device)
{
    m_activeGenericPhysicalDevices.removeAll(device);
}

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 18, as _ZN9Qt3DInput5Input24GenericDeviceBackendNodeC1EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DInput::Input {
inline GenericDeviceBackendNode::GenericDeviceBackendNode(QBackendNode::Mode mode)
    : QAbstractPhysicalDeviceBackendNode(mode)
    , m_mutex()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 24, as _ZN9Qt3DInput5Input24GenericDeviceBackendNodeD1Ev
namespace Qt3DInput::Input {
inline GenericDeviceBackendNode::~GenericDeviceBackendNode()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 28, as _ZN9Qt3DInput5Input24GenericDeviceBackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void GenericDeviceBackendNode::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QGenericInputDevice *node = qobject_cast<const Qt3DInput::QGenericInputDevice *>(frontEnd);
    if (!node)
        return;

    auto *d = static_cast<Qt3DInput::QAbstractPhysicalDevicePrivate *>( Qt3DCore::QNodePrivate::get(const_cast<Qt3DCore::QNode *>(frontEnd)) );

    {
        const QMutexLocker lock(&m_mutex);
        for (const auto &val: std::as_const(d->m_pendingAxisEvents))
            m_axesValues[val.first] = val.second;
        for (const auto &val: std::as_const(d->m_pendingButtonsEvents))
            m_buttonsValues[val.first] = val.second;

        d->m_pendingAxisEvents.clear();
        d->m_pendingButtonsEvents.clear();
    }
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 49, as _ZN9Qt3DInput5Input24GenericDeviceBackendNode7cleanupEv
namespace Qt3DInput::Input {
inline void GenericDeviceBackendNode::cleanup()
{
    const QMutexLocker lock(&m_mutex);
    m_axesValues.clear();
    m_buttonsValues.clear();
    QAbstractPhysicalDeviceBackendNode::cleanup();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 63, as _ZNK9Qt3DInput5Input24GenericDeviceBackendNode15isButtonPressedEi
namespace Qt3DInput::Input {
inline bool GenericDeviceBackendNode::isButtonPressed(int buttonIdentifier) const
{
    const QMutexLocker lock(&m_mutex);
    return m_buttonsValues[buttonIdentifier];
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 57, as _ZNK9Qt3DInput5Input24GenericDeviceBackendNode9axisValueEi
namespace Qt3DInput::Input {
inline float GenericDeviceBackendNode::axisValue(int axisIdentifier) const
{
    const QMutexLocker lock(&m_mutex);
    return m_axesValues[axisIdentifier];
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 69, as _ZN9Qt3DInput5Input27GenericDeviceBackendFunctorC1EPNS_12QInputAspectEPNS0_12InputHandlerE
namespace Qt3DInput::Input {
inline GenericDeviceBackendFunctor::GenericDeviceBackendFunctor(QInputAspect *inputaspect, InputHandler *handler)
    : m_inputAspect(inputaspect)
    , m_handler(handler)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 75, as _ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *GenericDeviceBackendFunctor::create(Qt3DCore::QNodeId id) const
{
    GenericDeviceBackendNode *backendNode = m_handler->genericDeviceBackendNodeManager()->getOrCreateResource(id);
    backendNode->setInputAspect(m_inputAspect);
    m_handler->appendGenericDevice(m_handler->genericDeviceBackendNodeManager()->lookupHandle(id));
    return backendNode;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 83, as _ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *GenericDeviceBackendFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_handler->genericDeviceBackendNodeManager()->lookupResource(id);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 88, as _ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline void GenericDeviceBackendFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_handler->removeGenericDevice(m_handler->genericDeviceBackendNodeManager()->lookupHandle(id));
    m_handler->genericDeviceBackendNodeManager()->releaseResource(id);
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::GenericDeviceBackendFunctor::GenericDeviceBackendFuncto
//      r(QInputAspect *inputaspect, InputHandler *handler)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::GenericDeviceBackendFunctor *ritual_ZN9Qt3DInput5Input27GenericDeviceBackendFunctorC1EPNS_12QInputAspectEPNS0_12InputHandlerE(
    Qt3DInput::QInputAspect *inputaspect,
    Qt3DInput::Input::InputHandler *handler) {
  return new Qt3DInput::Input::GenericDeviceBackendFunctor(
      inputaspect,
      handler);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::GenericDeviceBackendFunctor::create(Qt3DCore::QNod
//      eId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::GenericDeviceBackendFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::GenericDeviceBackendFunctor::get(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::GenericDeviceBackendFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void
//      Qt3DInput::Input::GenericDeviceBackendFunctor::destroy(Qt3DCore::QNod
//      eId id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::GenericDeviceBackendFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DInput::Input::GenericDeviceBackendFunctor::~GenericDeviceBackendFunct
//      or()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input27GenericDeviceBackendFunctorD1Ev(
    Qt3DInput::Input::GenericDeviceBackendFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::GenericDeviceBackendFunctor::create(Qt3DCore::QNod
//      eId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::GenericDeviceBackendFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DInput::Input::GenericDeviceBackendFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::GenericDeviceBackendFunctor::get(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::GenericDeviceBackendFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DInput::Input::GenericDeviceBackendFunctor::get(*id);
}

//  void
//      Qt3DInput::Input::GenericDeviceBackendFunctor::destroy(Qt3DCore::QNod
//      eId id) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9Qt3DInput5Input27GenericDeviceBackendFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::GenericDeviceBackendFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DInput::Input::GenericDeviceBackendFunctor::destroy(*id);
}
