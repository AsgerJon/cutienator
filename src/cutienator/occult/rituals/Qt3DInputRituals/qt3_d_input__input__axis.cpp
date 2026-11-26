//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/axis_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/axis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/axis_p.h>
#include <Qt3DInput/qaxis.h>
#include <Qt3DInput/qabstractaxisinput.h>
#include <Qt3DInput/private/qaxis_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/axis.cpp, line 18, as _ZN9Qt3DInput5Input4AxisC1Ev
namespace Qt3DInput::Input {
inline Axis::Axis()
    : BackendNode(ReadWrite)
    , m_axisValue(0.0f)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axis.cpp, line 24, as _ZN9Qt3DInput5Input4Axis7cleanupEv
namespace Qt3DInput::Input {
inline void Axis::cleanup()
{
    QBackendNode::setEnabled(false);
    m_inputs.clear();
    m_axisValue = 0.0f;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axis.cpp, line 31, as _ZN9Qt3DInput5Input4Axis12setAxisValueEf
namespace Qt3DInput::Input {
inline void Axis::setAxisValue(float axisValue)
{
    if (isEnabled() && (!qFuzzyCompare(axisValue, m_axisValue)))
        m_axisValue = axisValue;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axis.cpp, line 37, as _ZN9Qt3DInput5Input4Axis16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void Axis::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QAxis *node = qobject_cast<const Qt3DInput::QAxis *>(frontEnd);
    if (!node)
        return;

    auto ids = Qt3DCore::qIdsForNodes(node->inputs());
    m_inputs = ids;
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::Axis::Axis()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::Axis *ritual_ZN9Qt3DInput5Input4AxisC1Ev() {
  return new Qt3DInput::Input::Axis();
}

//  void Qt3DInput::Input::Axis::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input4Axis7cleanupEv(Qt3DInput::Input::Axis *self) {
  self->cleanup();
}

//  QList<Qt3DCore::QNodeId> Qt3DInput::Input::Axis::inputs() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK9Qt3DInput5Input4Axis6inputsEv(
    const Qt3DInput::Input::Axis *self) {
  return new QList<Qt3DCore::QNodeId>(self->inputs());
}

//  float Qt3DInput::Input::Axis::axisValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input4Axis9axisValueEv(
    const Qt3DInput::Input::Axis *self) {
  return self->axisValue();
}

//  void Qt3DInput::Input::Axis::setAxisValue(float axisValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input4Axis12setAxisValueEf(
    Qt3DInput::Input::Axis *self,
    float axisValue) {
  self->setAxisValue(axisValue);
}

//  void Qt3DInput::Input::Axis::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input4Axis16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::Axis *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::Axis::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input4Axis16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::Axis *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::Axis::syncFromFrontEnd(frontEnd, firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DInput::Input::Axis gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_Axis__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
