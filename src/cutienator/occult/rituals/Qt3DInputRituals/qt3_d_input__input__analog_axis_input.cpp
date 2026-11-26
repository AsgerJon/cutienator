//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/analogaxisinput_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/analogaxisinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/analogaxisinput_p.h>
#include <Qt3DInput/qanalogaxisinput.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/qabstractphysicaldevicebackendnode_p.h>
#include <Qt3DInput/private/qanalogaxisinput_p.h>
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

//  from ../qt3d/src/input/backend/analogaxisinput.cpp, line 41, as _ZN9Qt3DInput5Input15AnalogAxisInput7processEPNS0_12InputHandlerEx
namespace Qt3DInput::Input {
inline float AnalogAxisInput::process(InputHandler *inputHandler, qint64 currentTime)
{
    Q_UNUSED(currentTime);

    if (!isEnabled())
        return 0.0f;

    if (m_axis == -1)
        return 0.0f;

    QAbstractPhysicalDeviceBackendNode *physicalDeviceBackend = Utils::physicalDeviceForInput(this, inputHandler);
    if (!physicalDeviceBackend)
        return 0.0f;

    return physicalDeviceBackend->processedAxisValue(m_axis);
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

//  from ../qt3d/src/input/backend/analogaxisinput.cpp, line 25, as _ZN9Qt3DInput5Input15AnalogAxisInput7cleanupEv
namespace Qt3DInput::Input {
inline void AnalogAxisInput::cleanup()
{
    m_axis = 0;
    AbstractAxisInput::cleanup();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/analogaxisinput.cpp, line 31, as _ZN9Qt3DInput5Input15AnalogAxisInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void AnalogAxisInput::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    AbstractAxisInput::syncFromFrontEnd(frontEnd, firstTime);
    const QAnalogAxisInput *node = qobject_cast<const QAnalogAxisInput *>(frontEnd);
    if (!node)
        return;

    m_axis = node->axis();
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  void Qt3DInput::Input::AnalogAxisInput::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15AnalogAxisInput7cleanupEv(
    Qt3DInput::Input::AnalogAxisInput *self) {
  self->cleanup();
}

//  int Qt3DInput::Input::AnalogAxisInput::axis() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput5Input15AnalogAxisInput4axisEv(
    const Qt3DInput::Input::AnalogAxisInput *self) {
  return self->axis();
}

//  void Qt3DInput::Input::AnalogAxisInput::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input15AnalogAxisInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::AnalogAxisInput *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  float Qt3DInput::Input::AnalogAxisInput::process(InputHandler
//      *inputHandler, qint64 currentTime)
extern "C" Q_DECL_EXPORT
float ritual_ZN9Qt3DInput5Input15AnalogAxisInput7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::AnalogAxisInput *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->process(inputHandler, currentTime);
}

//  float Qt3DInput::Input::AnalogAxisInput::process(InputHandler
//      *inputHandler, qint64 currentTime)
extern "C" Q_DECL_EXPORT
float ritual_own_ZN9Qt3DInput5Input15AnalogAxisInput7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::AnalogAxisInput *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->Qt3DInput::Input::AnalogAxisInput::process(
      inputHandler,
      currentTime);
}
