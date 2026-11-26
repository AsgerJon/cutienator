//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/logicaldevice_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/logicaldevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/logicaldevice.cpp, line 19, as _ZN9Qt3DInput5Input13LogicalDeviceC1Ev
namespace Qt3DInput::Input {
inline LogicalDevice::LogicalDevice()
    : BackendNode()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/logicaldevice.cpp, line 24, as _ZN9Qt3DInput5Input13LogicalDevice7cleanupEv
namespace Qt3DInput::Input {
inline void LogicalDevice::cleanup()
{
    QBackendNode::setEnabled(false);
    m_actions.clear();
    m_axes.clear();
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
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::LogicalDevice::LogicalDevice()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::LogicalDevice *ritual_ZN9Qt3DInput5Input13LogicalDeviceC1Ev() {
  return new Qt3DInput::Input::LogicalDevice();
}

//  void Qt3DInput::Input::LogicalDevice::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input13LogicalDevice7cleanupEv(
    Qt3DInput::Input::LogicalDevice *self) {
  self->cleanup();
}

//  QList<Qt3DCore::QNodeId> Qt3DInput::Input::LogicalDevice::axes() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK9Qt3DInput5Input13LogicalDevice4axesEv(
    const Qt3DInput::Input::LogicalDevice *self) {
  return new QList<Qt3DCore::QNodeId>(self->axes());
}

//  QList<Qt3DCore::QNodeId> Qt3DInput::Input::LogicalDevice::actions() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK9Qt3DInput5Input13LogicalDevice7actionsEv(
    const Qt3DInput::Input::LogicalDevice *self) {
  return new QList<Qt3DCore::QNodeId>(self->actions());
}

//  void Qt3DInput::Input::LogicalDevice::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input13LogicalDevice16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::LogicalDevice *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::LogicalDevice::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input13LogicalDevice16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::LogicalDevice *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::LogicalDevice::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DInput::Input::LogicalDevice
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_LogicalDevice__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
