//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DLogic/6.12.0/Qt3DLogic/private/callbackjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DLogic/Qt3DLogic>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/6.12.0/Qt3DLogic/private/callbackjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/private/manager_p.h>
#include <Qt3DLogic/qlogicaspect.h>
#include <QtCore/QDebug>
#include <QtCore/QThread>
#include <QtCore/qcoreapplication.h>
#include <Qt3DCore/private/qabstractaspect_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/private/managers_p.h>
#include <Qt3DLogic/private/executor_p.h>
#include <Qt3DLogic/qframeaction.h>
#include <Qt3DCore/qnode.h>
#include <QtCore/qsemaphore.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DLogic/private/callbackjob_p.h>
#include <Qt3DLogic/private/job_common_p.h>
#include <Qt3DLogic/private/manager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qt3d/src/logic/callbackjob.cpp, line 14, as _ZN9Qt3DLogic5Logic11CallbackJobC1Ev
namespace Qt3DLogic::Logic {
inline CallbackJob::CallbackJob()
    : QAspectJob()
    , m_logicManager(nullptr)
{
    SET_JOB_RUN_STAT_TYPE(this, JobTypes::Callback, 0)
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/callbackjob.cpp, line 21, as _ZN9Qt3DLogic5Logic11CallbackJob10setManagerEPNS0_7ManagerE
namespace Qt3DLogic::Logic {
inline void CallbackJob::setManager(Manager *manager)
{
    m_logicManager = manager;
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/callbackjob.cpp, line 26, as _ZN9Qt3DLogic5Logic11CallbackJob3runEv
namespace Qt3DLogic::Logic {
inline void CallbackJob::run()
{
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/callbackjob.cpp, line 30, as _ZN9Qt3DLogic5Logic11CallbackJob10isRequiredEv
namespace Qt3DLogic::Logic {
inline bool CallbackJob::isRequired()
{
    return false;
}
}  // namespace Qt3DLogic::Logic

//  from ../qt3d/src/logic/callbackjob.cpp, line 35, as _ZN9Qt3DLogic5Logic11CallbackJob9postFrameEPN8Qt3DCore13QAspectEngineE
namespace Qt3DLogic::Logic {
inline void CallbackJob::postFrame(Qt3DCore::QAspectEngine *aspectEngine)
{
    Q_UNUSED(aspectEngine);
    Q_ASSERT(m_logicManager);
    m_logicManager->triggerLogicFrameUpdates();
}
}  // namespace Qt3DLogic::Logic
//  -----------------------------------------------------------------------

//  Qt3DLogic::Logic::CallbackJob::CallbackJob()
extern "C" Q_DECL_EXPORT
Qt3DLogic::Logic::CallbackJob *ritual_ZN9Qt3DLogic5Logic11CallbackJobC1Ev() {
  return new Qt3DLogic::Logic::CallbackJob();
}

//  void Qt3DLogic::Logic::CallbackJob::setManager(Manager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic11CallbackJob10setManagerEPNS0_7ManagerE(
    Qt3DLogic::Logic::CallbackJob *self,
    Qt3DLogic::Logic::Manager *manager) {
  self->setManager(manager);
}

//  void Qt3DLogic::Logic::CallbackJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic11CallbackJob3runEv(
    Qt3DLogic::Logic::CallbackJob *self) {
  self->run();
}

//  bool Qt3DLogic::Logic::CallbackJob::isRequired()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9Qt3DLogic5Logic11CallbackJob10isRequiredEv(
    Qt3DLogic::Logic::CallbackJob *self) {
  return self->isRequired();
}

//  void Qt3DLogic::Logic::CallbackJob::postFrame(Qt3DCore::QAspectEngine
//      *aspectEngine)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic11CallbackJob9postFrameEPN8Qt3DCore13QAspectEngineE(
    Qt3DLogic::Logic::CallbackJob *self,
    Qt3DCore::QAspectEngine *aspectEngine) {
  self->postFrame(aspectEngine);
}

//  void Qt3DLogic::Logic::CallbackJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DLogic5Logic11CallbackJob3runEv(
    Qt3DLogic::Logic::CallbackJob *self) {
  self->Qt3DLogic::Logic::CallbackJob::run();
}

//  bool Qt3DLogic::Logic::CallbackJob::isRequired()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9Qt3DLogic5Logic11CallbackJob10isRequiredEv(
    Qt3DLogic::Logic::CallbackJob *self) {
  return self->Qt3DLogic::Logic::CallbackJob::isRequired();
}

//  void Qt3DLogic::Logic::CallbackJob::postFrame(Qt3DCore::QAspectEngine
//      *aspectEngine)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DLogic5Logic11CallbackJob9postFrameEPN8Qt3DCore13QAspectEngineE(
    Qt3DLogic::Logic::CallbackJob *self,
    Qt3DCore::QAspectEngine *aspectEngine) {
  self->Qt3DLogic::Logic::CallbackJob::postFrame(aspectEngine);
}
