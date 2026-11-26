//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/inputsettings_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/inputsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/inputsettings_p.h>
#include <Qt3DInput/qinputsettings.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qinputsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  Qt3DInput::Input::InputSettings::InputSettings()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::InputSettings *ritual_ZN9Qt3DInput5Input13InputSettingsC1Ev() {
  return new Qt3DInput::Input::InputSettings();
}

//  QObject *Qt3DInput::Input::InputSettings::eventSource() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK9Qt3DInput5Input13InputSettings11eventSourceEv(
    const Qt3DInput::Input::InputSettings *self) {
  return self->eventSource();
}

//  void Qt3DInput::Input::InputSettings::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input13InputSettings16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::InputSettings *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::InputSettings::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input13InputSettings16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::InputSettings *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::InputSettings::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
