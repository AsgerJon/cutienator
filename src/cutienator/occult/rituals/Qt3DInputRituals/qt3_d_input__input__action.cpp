//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/action_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/action_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/action_p.h>
#include <Qt3DInput/qaction.h>
#include <Qt3DInput/qabstractactioninput.h>
#include <Qt3DInput/private/qaction_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/action.cpp, line 17, as _ZN9Qt3DInput5Input6ActionC1Ev
namespace Qt3DInput::Input {
inline Action::Action()
    : BackendNode(ReadWrite)
    , m_actionTriggered(false)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/action.cpp, line 23, as _ZN9Qt3DInput5Input6Action7cleanupEv
namespace Qt3DInput::Input {
inline void Action::cleanup()
{
    QBackendNode::setEnabled(false);
    m_inputs.clear();
    m_actionTriggered = false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/action.cpp, line 30, as _ZN9Qt3DInput5Input6Action18setActionTriggeredEb
namespace Qt3DInput::Input {
inline void Action::setActionTriggered(bool actionTriggered)
{
    if (isEnabled() && (actionTriggered != m_actionTriggered))
        m_actionTriggered = actionTriggered;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/action.cpp, line 36, as _ZN9Qt3DInput5Input6Action16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void Action::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QAction *node = qobject_cast<const Qt3DInput::QAction *>(frontEnd);
    if (!node)
        return;

    auto ids = Qt3DCore::qIdsForNodes(node->inputs());
    m_inputs = ids;
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::Action::Action()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::Action *ritual_ZN9Qt3DInput5Input6ActionC1Ev() {
  return new Qt3DInput::Input::Action();
}

//  void Qt3DInput::Input::Action::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input6Action7cleanupEv(
    Qt3DInput::Input::Action *self) {
  self->cleanup();
}

//  QList<Qt3DCore::QNodeId> Qt3DInput::Input::Action::inputs() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK9Qt3DInput5Input6Action6inputsEv(
    const Qt3DInput::Input::Action *self) {
  return new QList<Qt3DCore::QNodeId>(self->inputs());
}

//  bool Qt3DInput::Input::Action::actionTriggered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput5Input6Action15actionTriggeredEv(
    const Qt3DInput::Input::Action *self) {
  return self->actionTriggered();
}

//  void Qt3DInput::Input::Action::setActionTriggered(bool actionTriggered)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input6Action18setActionTriggeredEb(
    Qt3DInput::Input::Action *self,
    bool actionTriggered) {
  self->setActionTriggered(actionTriggered);
}

//  void Qt3DInput::Input::Action::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input6Action16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::Action *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DInput::Input::Action::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input6Action16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::Action *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::Action::syncFromFrontEnd(frontEnd, firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DInput::Input::Action gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_Action__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
