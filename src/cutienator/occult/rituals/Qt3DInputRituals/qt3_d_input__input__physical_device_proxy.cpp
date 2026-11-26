//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/physicaldeviceproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/physicaldeviceproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 19, as _ZN9Qt3DInput5Input19PhysicalDeviceProxyC1Ev
namespace Qt3DInput::Input {
inline PhysicalDeviceProxy::PhysicalDeviceProxy()
    : BackendNode(QBackendNode::ReadWrite)
    , m_manager(nullptr)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 25, as _ZN9Qt3DInput5Input19PhysicalDeviceProxy7cleanupEv
namespace Qt3DInput::Input {
inline void PhysicalDeviceProxy::cleanup()
{
    QBackendNode::setEnabled(false);
    m_deviceName.clear();
    m_manager = nullptr;
    m_physicalDeviceId = Qt3DCore::QNodeId();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 33, as _ZNK9Qt3DInput5Input19PhysicalDeviceProxy10deviceNameEv
namespace Qt3DInput::Input {
inline QString PhysicalDeviceProxy::deviceName() const
{
    return m_deviceName;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 38, as _ZN9Qt3DInput5Input19PhysicalDeviceProxy10setManagerEPNS0_26PhysicalDeviceProxyManagerE
namespace Qt3DInput::Input {
inline void PhysicalDeviceProxy::setManager(PhysicalDeviceProxyManager *manager)
{
    m_manager = manager;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 43, as _ZNK9Qt3DInput5Input19PhysicalDeviceProxy7managerEv
namespace Qt3DInput::Input {
inline PhysicalDeviceProxyManager *PhysicalDeviceProxy::manager() const
{
    return m_manager;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 48, as _ZN9Qt3DInput5Input19PhysicalDeviceProxy9setDeviceEPNS_23QAbstractPhysicalDeviceE
namespace Qt3DInput::Input {
inline void PhysicalDeviceProxy::setDevice(QAbstractPhysicalDevice *device)
{
    m_physicalDeviceId = Qt3DCore::QNodeId();
    // Move the device to the main thread
    if (device != nullptr) {
        m_physicalDeviceId = device->id();
        device->moveToThread(QCoreApplication::instance()->thread());
    }
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 58, as _ZNK9Qt3DInput5Input19PhysicalDeviceProxy16physicalDeviceIdEv
namespace Qt3DInput::Input {
inline Qt3DCore::QNodeId PhysicalDeviceProxy::physicalDeviceId() const
{
    return m_physicalDeviceId;
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
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::PhysicalDeviceProxy::PhysicalDeviceProxy()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::PhysicalDeviceProxy *ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxyC1Ev() {
  return new Qt3DInput::Input::PhysicalDeviceProxy();
}

//  void Qt3DInput::Input::PhysicalDeviceProxy::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxy7cleanupEv(
    Qt3DInput::Input::PhysicalDeviceProxy *self) {
  self->cleanup();
}

//  QString Qt3DInput::Input::PhysicalDeviceProxy::deviceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9Qt3DInput5Input19PhysicalDeviceProxy10deviceNameEv(
    const Qt3DInput::Input::PhysicalDeviceProxy *self) {
  return new QString(self->deviceName());
}

//  void Qt3DInput::Input::PhysicalDeviceProxy::setManager(PhysicalDeviceProx
//      yManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxy10setManagerEPNS0_26PhysicalDeviceProxyManagerE(
    Qt3DInput::Input::PhysicalDeviceProxy *self,
    Qt3DInput::Input::PhysicalDeviceProxyManager *manager) {
  self->setManager(manager);
}

//  PhysicalDeviceProxyManager
//      *Qt3DInput::Input::PhysicalDeviceProxy::manager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::PhysicalDeviceProxyManager *ritual_ZNK9Qt3DInput5Input19PhysicalDeviceProxy7managerEv(
    const Qt3DInput::Input::PhysicalDeviceProxy *self) {
  return self->manager();
}

//  void
//      Qt3DInput::Input::PhysicalDeviceProxy::setDevice(QAbstractPhysicalDev
//      ice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxy9setDeviceEPNS_23QAbstractPhysicalDeviceE(
    Qt3DInput::Input::PhysicalDeviceProxy *self,
    Qt3DInput::QAbstractPhysicalDevice *device) {
  self->setDevice(device);
}

//  Qt3DCore::QNodeId
//      Qt3DInput::Input::PhysicalDeviceProxy::physicalDeviceId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK9Qt3DInput5Input19PhysicalDeviceProxy16physicalDeviceIdEv(
    const Qt3DInput::Input::PhysicalDeviceProxy *self) {
  return new Qt3DCore::QNodeId(self->physicalDeviceId());
}

//  void Qt3DInput::Input::PhysicalDeviceProxy::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input19PhysicalDeviceProxy16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::PhysicalDeviceProxy *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::PhysicalDeviceProxy::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input19PhysicalDeviceProxy16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::PhysicalDeviceProxy *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::PhysicalDeviceProxy::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
