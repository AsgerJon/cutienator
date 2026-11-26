//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/physicaldeviceproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/physicaldeviceproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 38, as _ZN9Qt3DInput5Input19PhysicalDeviceProxy10setManagerEPNS0_26PhysicalDeviceProxyManagerE
namespace Qt3DInput::Input {
inline void PhysicalDeviceProxy::setManager(PhysicalDeviceProxyManager *manager)
{
    m_manager = manager;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 19, as _ZN9Qt3DInput5Input19PhysicalDeviceProxyC1Ev
namespace Qt3DInput::Input {
inline PhysicalDeviceProxy::PhysicalDeviceProxy()
    : BackendNode(QBackendNode::ReadWrite)
    , m_manager(nullptr)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 63, as _ZN9Qt3DInput5Input19PhysicalDeviceProxy16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void PhysicalDeviceProxy::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);

    if (firstTime) {
        const QAbstractPhysicalDeviceProxy *node = qobject_cast<const QAbstractPhysicalDeviceProxy *>(frontEnd);
        if (!node)
            return;

        m_deviceName = node->deviceName();

        // Request to load the actual device
        m_manager->addPendingProxyToLoad(peerId());
    }
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 92, as _ZNK9Qt3DInput5Input30PhysicalDeviceProxyNodeFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *PhysicalDeviceProxyNodeFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_manager->lookupResource(id);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 97, as _ZNK9Qt3DInput5Input30PhysicalDeviceProxyNodeFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline void PhysicalDeviceProxyNodeFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_manager->releaseResource(id);
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::PhysicalDeviceProxyNodeFunctor::get(Qt3DCore::QNod
//      eId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input30PhysicalDeviceProxyNodeFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::PhysicalDeviceProxyNodeFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DInput::Input::PhysicalDeviceProxyNodeFunctor::destroy(Qt3DCore::
//      QNodeId id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9Qt3DInput5Input30PhysicalDeviceProxyNodeFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::PhysicalDeviceProxyNodeFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DInput::Input::PhysicalDeviceProxyNodeFunctor::~PhysicalDeviceProxyNod
//      eFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input30PhysicalDeviceProxyNodeFunctorD1Ev(
    Qt3DInput::Input::PhysicalDeviceProxyNodeFunctor *self) {
  delete self;
}
