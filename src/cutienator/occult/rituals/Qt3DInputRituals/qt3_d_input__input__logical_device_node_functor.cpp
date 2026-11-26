//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/logicaldevice_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/logicaldevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/logicaldevice_p.h>
#include <Qt3DInput/qaction.h>
#include <Qt3DInput/qaxis.h>
#include <Qt3DInput/qlogicaldevice.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qlogicaldevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/logicaldevice.cpp, line 19, as _ZN9Qt3DInput5Input13LogicalDeviceC1Ev
namespace Qt3DInput::Input {
inline LogicalDevice::LogicalDevice()
    : BackendNode()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/logicaldevice.cpp, line 31, as _ZN9Qt3DInput5Input13LogicalDevice16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void LogicalDevice::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QLogicalDevice *node = qobject_cast<const QLogicalDevice *>(frontEnd);
    if (!node)
        return;

    m_actions = Qt3DCore::qIdsForNodes(node->actions());
    m_axes = Qt3DCore::qIdsForNodes(node->axes());
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/logicaldevice.cpp, line 42, as _ZN9Qt3DInput5Input24LogicalDeviceNodeFunctorC1EPNS0_20LogicalDeviceManagerE
namespace Qt3DInput::Input {
inline LogicalDeviceNodeFunctor::LogicalDeviceNodeFunctor(LogicalDeviceManager *manager)
    : m_manager(manager)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/logicaldevice.cpp, line 47, as _ZNK9Qt3DInput5Input24LogicalDeviceNodeFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *LogicalDeviceNodeFunctor::create(Qt3DCore::QNodeId id) const
{
    HLogicalDevice handle = m_manager->getOrAcquireHandle(id);
    LogicalDevice *backend = m_manager->data(handle);
    m_manager->addActiveDevice(handle);
    return backend;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/logicaldevice.cpp, line 55, as _ZNK9Qt3DInput5Input24LogicalDeviceNodeFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *LogicalDeviceNodeFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_manager->lookupResource(id);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/logicaldevice.cpp, line 60, as _ZNK9Qt3DInput5Input24LogicalDeviceNodeFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline void LogicalDeviceNodeFunctor::destroy(Qt3DCore::QNodeId id) const
{
    HLogicalDevice handle = m_manager->lookupHandle(id);
    m_manager->releaseResource(id);
    m_manager->removeActiveDevice(handle);
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::LogicalDeviceNodeFunctor::LogicalDeviceNodeFunctor(Logi
//      calDeviceManager *manager)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::LogicalDeviceNodeFunctor *ritual_ZN9Qt3DInput5Input24LogicalDeviceNodeFunctorC1EPNS0_20LogicalDeviceManagerE(
    Qt3DInput::Input::LogicalDeviceManager *manager) {
  return new Qt3DInput::Input::LogicalDeviceNodeFunctor(manager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::LogicalDeviceNodeFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input24LogicalDeviceNodeFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::LogicalDeviceNodeFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::LogicalDeviceNodeFunctor::get(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input24LogicalDeviceNodeFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::LogicalDeviceNodeFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void
//      Qt3DInput::Input::LogicalDeviceNodeFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9Qt3DInput5Input24LogicalDeviceNodeFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::LogicalDeviceNodeFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DInput::Input::LogicalDeviceNodeFunctor::~LogicalDeviceNodeFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input24LogicalDeviceNodeFunctorD1Ev(
    Qt3DInput::Input::LogicalDeviceNodeFunctor *self) {
  delete self;
}
