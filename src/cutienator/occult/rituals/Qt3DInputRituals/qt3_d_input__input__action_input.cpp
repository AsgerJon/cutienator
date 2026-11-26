//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/actioninput_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/actioninput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/abstractactioninput_p.h>
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
#include <Qt3DInput/private/actioninput_p.h>
#include <Qt3DInput/qactioninput.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/qactioninput_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/abstractactioninput.cpp, line 12, as _ZN9Qt3DInput5Input19AbstractActionInputC2Ev
namespace Qt3DInput::Input {
inline AbstractActionInput::AbstractActionInput()
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

//  from ../qt3d/src/input/backend/actioninput.cpp, line 18, as _ZN9Qt3DInput5Input11ActionInputC1Ev
namespace Qt3DInput::Input {
inline ActionInput::ActionInput()
    : AbstractActionInput()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/actioninput.cpp, line 23, as _ZN9Qt3DInput5Input11ActionInput7cleanupEv
namespace Qt3DInput::Input {
inline void ActionInput::cleanup()
{
    setEnabled(false);
    m_sourceDevice = Qt3DCore::QNodeId();
    m_buttons.clear();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/actioninput.cpp, line 30, as _ZN9Qt3DInput5Input11ActionInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void ActionInput::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    AbstractActionInput::syncFromFrontEnd(frontEnd, firstTime);
    const QActionInput *node = qobject_cast<const QActionInput *>(frontEnd);
    if (!node)
        return;

    m_sourceDevice = Qt3DCore::qIdForNode(node->sourceDevice());
    m_buttons = node->buttons();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/actioninput.cpp, line 41, as _ZN9Qt3DInput5Input11ActionInput7processEPNS0_12InputHandlerEx
namespace Qt3DInput::Input {
inline bool ActionInput::process(InputHandler *inputHandler, qint64 currentTime)
{
    Q_UNUSED(currentTime);

    if (!isEnabled())
        return false;

    QAbstractPhysicalDeviceBackendNode *physicalDeviceBackend = Utils::physicalDeviceForInput(this, inputHandler);
    if (!physicalDeviceBackend)
        return false;

    for (int button : std::as_const(m_buttons)) {
        if (physicalDeviceBackend->isButtonPressed(button))
            return true;
    }

    return false;
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::ActionInput::ActionInput()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::ActionInput *ritual_ZN9Qt3DInput5Input11ActionInputC1Ev() {
  return new Qt3DInput::Input::ActionInput();
}

//  void Qt3DInput::Input::ActionInput::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input11ActionInput7cleanupEv(
    Qt3DInput::Input::ActionInput *self) {
  self->cleanup();
}

//  QList<int> Qt3DInput::Input::ActionInput::buttons() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK9Qt3DInput5Input11ActionInput7buttonsEv(
    const Qt3DInput::Input::ActionInput *self) {
  return new QList<int>(self->buttons());
}

//  Qt3DCore::QNodeId Qt3DInput::Input::ActionInput::sourceDevice() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK9Qt3DInput5Input11ActionInput12sourceDeviceEv(
    const Qt3DInput::Input::ActionInput *self) {
  return new Qt3DCore::QNodeId(self->sourceDevice());
}

//  void Qt3DInput::Input::ActionInput::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input11ActionInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::ActionInput *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  bool Qt3DInput::Input::ActionInput::process(InputHandler *inputHandler,
//      qint64 currentTime)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9Qt3DInput5Input11ActionInput7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::ActionInput *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->process(inputHandler, currentTime);
}

//  void Qt3DInput::Input::ActionInput::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input11ActionInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::ActionInput *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::ActionInput::syncFromFrontEnd(frontEnd, firstTime);
}

//  bool Qt3DInput::Input::ActionInput::process(InputHandler *inputHandler,
//      qint64 currentTime)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9Qt3DInput5Input11ActionInput7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::ActionInput *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->Qt3DInput::Input::ActionInput::process(
      inputHandler,
      currentTime);
}

//  a QList<int> a ritual of Qt3DInput::Input::ActionInput gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_ActionInput__QList_int(QList<int> *self) {
  delete self;
}
