//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/inputsettings_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/inputsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/inputsettings_p.h>
#include <Qt3DInput/qinputsettings.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qinputsettings_p.h>
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

//  from ../qt3d/src/input/backend/inputsettings.cpp, line 38, as _ZNK9Qt3DInput5Input20InputSettingsFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *InputSettingsFunctor::create(Qt3DCore::QNodeId id) const
{
    Q_UNUSED(id);
    if (m_handler->inputSettings() != nullptr) {
        qWarning() << "Input settings already specified";
        return nullptr;
    }

    InputSettings *settings = new InputSettings();
    m_handler->setInputSettings(settings);
    return settings;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsettings.cpp, line 51, as _ZNK9Qt3DInput5Input20InputSettingsFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline Qt3DCore::QBackendNode *InputSettingsFunctor::get(Qt3DCore::QNodeId id) const
{
    InputSettings *settings = m_handler->inputSettings();
    if (settings != nullptr && settings->peerId() == id)
        return settings;
    return nullptr;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsettings.cpp, line 59, as _ZNK9Qt3DInput5Input20InputSettingsFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline void InputSettingsFunctor::destroy(Qt3DCore::QNodeId id) const
{
    InputSettings *settings = m_handler->inputSettings();
    if (settings != nullptr && settings->peerId() == id) {
        m_handler->setInputSettings(nullptr);
        delete settings;
    }
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 134, as _ZN9Qt3DInput5Input12InputHandler16setInputSettingsEPNS0_13InputSettingsE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::setInputSettings(InputSettings *settings)
{
    if (m_settings && settings == nullptr) {
        unregisterEventFilters();
        m_lastEventSource = nullptr;
        if (m_settings->eventSource() && m_service)
            m_service->shutdown(m_settings->eventSource());
    }
    if (m_service) {
        unregisterEventFilters();
        if (m_settings && m_settings->eventSource())
            m_service->shutdown(m_settings->eventSource());
    }
    m_settings = settings;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsettings.cpp, line 17, as _ZN9Qt3DInput5Input13InputSettingsC1Ev
namespace Qt3DInput::Input {
inline InputSettings::InputSettings()
    : BackendNode(QBackendNode::ReadOnly)
    , m_eventSource(nullptr)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsettings.cpp, line 23, as _ZN9Qt3DInput5Input13InputSettings16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void InputSettings::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QInputSettings *node = qobject_cast<const QInputSettings *>(frontEnd);
    if (!node)
        return;

    m_eventSource = node->eventSource();
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::InputSettingsFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input20InputSettingsFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::InputSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::InputSettingsFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK9Qt3DInput5Input20InputSettingsFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::InputSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DInput::Input::InputSettingsFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9Qt3DInput5Input20InputSettingsFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::InputSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DInput::Input::InputSettingsFunctor::~InputSettingsFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input20InputSettingsFunctorD1Ev(
    Qt3DInput::Input::InputSettingsFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DInput::Input::InputSettingsFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK9Qt3DInput5Input20InputSettingsFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::InputSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DInput::Input::InputSettingsFunctor::get(*id);
}
