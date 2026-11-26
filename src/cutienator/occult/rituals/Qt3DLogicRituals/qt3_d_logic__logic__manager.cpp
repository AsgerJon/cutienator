//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DLogic/6.12.0/Qt3DLogic/private/manager_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DLogic/Qt3DLogic>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/6.12.0/Qt3DLogic/private/manager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/qframeaction.h>
#include <Qt3DCore/qnode.h>
#include <QtCore/qsemaphore.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DLogic/private/manager_p.h>
#include <Qt3DLogic/qlogicaspect.h>
#include <QtCore/QDebug>
#include <QtCore/QThread>
#include <QtCore/qcoreapplication.h>
#include <Qt3DCore/private/qabstractaspect_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/logic/executor.cpp, line 29, as _ZN9Qt3DLogic5Logic8Executor24processLogicFrameUpdatesERK5QListIN8Qt3DCore7QNodeIdEEf
namespace Qt3DLogic::Logic {
using namespace Qt3DCore;
inline void Executor::processLogicFrameUpdates(const QList<QNodeId> &nodeIds, float dt)
{
    if (!m_scene || nodeIds.isEmpty())
        return;

    const QList<QNode *> nodes = m_scene->lookupNodes(nodeIds);
    for (QNode *node : nodes) {
        QFrameAction *frameAction = qobject_cast<QFrameAction *>(node);
        if (frameAction && frameAction->isEnabled())
            frameAction->onTriggered(dt);
    }
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 21, as _ZN9Qt3DLogic5Logic7ManagerC1Ev
namespace Qt3DLogic::Logic {
inline Manager::Manager()
    : m_logicHandlerManager(new HandlerManager)
    , m_logicAspect(nullptr)
    , m_executor(nullptr)
    , m_dt(0.0f)
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 29, as _ZN9Qt3DLogic5Logic7ManagerD1Ev
namespace Qt3DLogic::Logic {
inline Manager::~Manager()
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 33, as _ZN9Qt3DLogic5Logic7Manager11setExecutorEPNS0_8ExecutorE
namespace Qt3DLogic::Logic {
inline void Manager::setExecutor(Executor *executor)
{
    m_executor = executor;
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 38, as _ZN9Qt3DLogic5Logic7Manager13appendHandlerEPNS0_7HandlerE
namespace Qt3DLogic::Logic {
inline void Manager::appendHandler(Handler *handler)
{
    HHandler handle = m_logicHandlerManager->lookupHandle(handler->peerId());
    if (!m_logicHandlers.contains(handle)) {
        m_logicHandlers.append(handle);
        m_logicComponentIds.append(handler->peerId());
    }
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 47, as _ZN9Qt3DLogic5Logic7Manager13removeHandlerEN8Qt3DCore7QNodeIdE
namespace Qt3DLogic::Logic {
inline void Manager::removeHandler(Qt3DCore::QNodeId id)
{
    HHandler handle = m_logicHandlerManager->lookupHandle(id);
    m_logicComponentIds.removeAll(id);
    m_logicHandlers.removeAll(handle);
    m_logicHandlerManager->releaseResource(id);
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 55, as _ZNK9Qt3DLogic5Logic7Manager15hasFrameActionsEv
namespace Qt3DLogic::Logic {
inline bool Manager::hasFrameActions() const
{
    return m_logicHandlers.size() > 0;
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/manager.cpp, line 61, as _ZN9Qt3DLogic5Logic7Manager24triggerLogicFrameUpdatesEv
namespace Qt3DLogic::Logic {
inline void Manager::triggerLogicFrameUpdates()
{
    Q_ASSERT(m_executor);

    // Don't use blocking queued connections to main thread if it is already
    // in the process of shutting down as that will deadlock.
    if (Qt3DCore::QAbstractAspectPrivate::get(m_logicAspect)->m_aspectManager->isShuttingDown())
        return;

    m_executor->processLogicFrameUpdates(m_logicComponentIds, m_dt);
}
}  // namespace Qt3DLogic::Logic
//  -----------------------------------------------------------------------

//  Qt3DLogic::Logic::Manager::Manager()
extern "C" Q_DECL_EXPORT
Qt3DLogic::Logic::Manager *ritual_ZN9Qt3DLogic5Logic7ManagerC1Ev() {
  return new Qt3DLogic::Logic::Manager();
}

//  Qt3DLogic::Logic::Manager::~Manager()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7ManagerD1Ev(Qt3DLogic::Logic::Manager *self) {
  delete self;
}

//  void Qt3DLogic::Logic::Manager::setLogicAspect(QLogicAspect *logicAspect)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Manager14setLogicAspectEPNS_12QLogicAspectE(
    Qt3DLogic::Logic::Manager *self,
    Qt3DLogic::QLogicAspect *logicAspect) {
  self->setLogicAspect(logicAspect);
}

//  void Qt3DLogic::Logic::Manager::setExecutor(Executor *executor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Manager11setExecutorEPNS0_8ExecutorE(
    Qt3DLogic::Logic::Manager *self,
    Qt3DLogic::Logic::Executor *executor) {
  self->setExecutor(executor);
}

//  HandlerManager *Qt3DLogic::Logic::Manager::logicHandlerManager() const
extern "C" Q_DECL_EXPORT
Qt3DLogic::Logic::HandlerManager *ritual_ZNK9Qt3DLogic5Logic7Manager19logicHandlerManagerEv(
    const Qt3DLogic::Logic::Manager *self) {
  return self->logicHandlerManager();
}

//  void Qt3DLogic::Logic::Manager::appendHandler(Handler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Manager13appendHandlerEPNS0_7HandlerE(
    Qt3DLogic::Logic::Manager *self,
    Qt3DLogic::Logic::Handler *handler) {
  self->appendHandler(handler);
}

//  void Qt3DLogic::Logic::Manager::removeHandler(Qt3DCore::QNodeId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Manager13removeHandlerEN8Qt3DCore7QNodeIdE(
    Qt3DLogic::Logic::Manager *self,
    const Qt3DCore::QNodeId *id) {
  self->removeHandler(*id);
}

//  bool Qt3DLogic::Logic::Manager::hasFrameActions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DLogic5Logic7Manager15hasFrameActionsEv(
    const Qt3DLogic::Logic::Manager *self) {
  return self->hasFrameActions();
}

//  void Qt3DLogic::Logic::Manager::triggerLogicFrameUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Manager24triggerLogicFrameUpdatesEv(
    Qt3DLogic::Logic::Manager *self) {
  self->triggerLogicFrameUpdates();
}

//  void Qt3DLogic::Logic::Manager::setDeltaTime(float dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic7Manager12setDeltaTimeEf(
    Qt3DLogic::Logic::Manager *self,
    float dt) {
  self->setDeltaTime(dt);
}
