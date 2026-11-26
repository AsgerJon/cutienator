//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/axissetting_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/axissetting_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/axissetting_p.h>
#include <Qt3DInput/qaxissetting.h>
#include <Qt3DInput/private/qaxissetting_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/axissetting.cpp, line 15, as _ZN9Qt3DInput5Input11AxisSettingC1Ev
namespace Qt3DInput::Input {
inline AxisSetting::AxisSetting()
    : BackendNode()
    , m_deadZoneRadius(0.0f)
    , m_smooth(false)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axissetting.cpp, line 22, as _ZN9Qt3DInput5Input11AxisSetting7cleanupEv
namespace Qt3DInput::Input {
inline void AxisSetting::cleanup()
{
    QBackendNode::setEnabled(false);
    m_deadZoneRadius = 0.0f;
    m_axes.clear();
    m_smooth = false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axissetting.cpp, line 30, as _ZN9Qt3DInput5Input11AxisSetting16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void AxisSetting::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QAxisSetting *node = qobject_cast<const QAxisSetting *>(frontEnd);
    if (!node)
        return;

    m_deadZoneRadius = node->deadZoneRadius();
    m_axes = node->axes();
    m_smooth = node->isSmoothEnabled();
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::AxisSetting::AxisSetting()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AxisSetting *ritual_ZN9Qt3DInput5Input11AxisSettingC1Ev() {
  return new Qt3DInput::Input::AxisSetting();
}

//  void Qt3DInput::Input::AxisSetting::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input11AxisSetting7cleanupEv(
    Qt3DInput::Input::AxisSetting *self) {
  self->cleanup();
}

//  float Qt3DInput::Input::AxisSetting::deadZoneRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input11AxisSetting14deadZoneRadiusEv(
    const Qt3DInput::Input::AxisSetting *self) {
  return self->deadZoneRadius();
}

//  QList<int> Qt3DInput::Input::AxisSetting::axes() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK9Qt3DInput5Input11AxisSetting4axesEv(
    const Qt3DInput::Input::AxisSetting *self) {
  return new QList<int>(self->axes());
}

//  bool Qt3DInput::Input::AxisSetting::isSmoothEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput5Input11AxisSetting15isSmoothEnabledEv(
    const Qt3DInput::Input::AxisSetting *self) {
  return self->isSmoothEnabled();
}

//  void Qt3DInput::Input::AxisSetting::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input11AxisSetting16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::AxisSetting *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::AxisSetting::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input11AxisSetting16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::AxisSetting *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::AxisSetting::syncFromFrontEnd(frontEnd, firstTime);
}

//  a QList<int> a ritual of Qt3DInput::Input::AxisSetting gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_AxisSetting__QList_int(QList<int> *self) {
  delete self;
}
